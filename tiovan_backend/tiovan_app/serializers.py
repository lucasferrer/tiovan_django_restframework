from rest_framework import serializers

from django.contrib.auth.models import User, Group
from tiovan_app.models import Motorista, Endereco



# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         # exclude = ['password']
#         fields = ['id','url', 'username', 'email','password'] 

#         extra_kwargs = {
#             "password": {"write_only": True},
#         }

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
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


class MotoristaSerializer(serializers.ModelSerializer):
    # nome = serializers.CharField(min_length=2, max_length=200)
    # email = serializers.CharField(min_length=2, max_length=200)
    # cpf = serializers.CharField(min_length=2, max_length=200)
    # endereco = serializers.ForeignKey(Endereco, on_delete=models.CASCADE, default=None)
    # senha = serializers.CharField(max_length=100, default=None)
    # imagem = serializers.ImageField(upload_to='images/', null=True)

    class Meta:
        model = Motorista
        fields = '__all__'


class MotoristaDetailSerializer(serializers.ModelSerializer):
    endereco = EnderecoSerializer(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Motorista
        fields = '__all__'



def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserSerializer(user, context={'request': request}).data
    }