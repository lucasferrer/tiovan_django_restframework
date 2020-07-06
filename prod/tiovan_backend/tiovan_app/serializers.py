from rest_framework import serializers
import requests, json
from django.contrib.auth.models import User, Group
from tiovan_app.models import Motorista, Endereco, Instituicoes, Responsavel, Dependente
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
        'id',
        'username',
        'email',
        'password',
       ]
        extra_kwargs = {
        'password': {'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields = '__all__'
    
    def create(self, validated_data):
        try:
            instance = self.Meta.model(**validated_data)
            url = 'https://maps.googleapis.com/maps/api/geocode/json'
            params = {'sensor': 'false', 'address': f'{instance.logradouro} {instance.numero}\
                 {instance.cidade}, {instance.bairro}, {instance.uf}, cep {instance.cep}',\
                 'key': 'AIzaSyAcmj2YYRcITWxouB3W6Lv3rEtgBjpVVw4'}
            r = requests.get(url, params=params)
            print(r.json)
            if r.json()['results'] == []:
                raise ValidationError({'Erro': 'Endereco invalido'})
            else:
                results = r.json()['results']
                location = results[0]['geometry']['location']
                print(location)
                instance.latitude = location['lat']
                instance.longitude = location['lng']
                instance.save()
                return instance
        except Exception as e:
            print(e)


class InstituicoesSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Instituicoes
        fields = '__all__'


class ResponsavelSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Responsavel
        fields = '__all__'


class DependenteSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Dependente
        fields = '__all__'


class MotoristaSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Motorista
        fields = '__all__'


class MotoristaDetailSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Motorista
        fields = '__all__'


class ResponsavelDetailSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)

    class Meta:
        model = Responsavel
        fields = '__all__'


class InstituicoesDetailSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)

    class Meta:
        model = Instituicoes
        fields = '__all__'


class DependenteDetailSerializer(serializers.ModelSerializer):
    instituicao = InstituicoesDetailSerializer(read_only=True)
    responsavel = ResponsavelDetailSerializer(read_only=True)
    # motorista = instituicao['motorista']

    class Meta:
        model = Dependente
        fields = '__all__'



def jwt_response_payload_handler(token, usuario=None, request=None):
    usuario = UserSerializer(usuario, context={'request': request}).data
    motorista = Motorista.objects.filter(user = usuario['id'])
    motorista = get_object_or_404(motorista, user = usuario['id'])
    motorista = MotoristaDetailSerializer(motorista, context={'request': request})
    return {
        'token': token,
        'motorista': motorista.data
    }