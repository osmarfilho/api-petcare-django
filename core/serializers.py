from rest_framework import serializers
from .models import ONG, Animal, ConsultaVeterinaria, Adotante

class ONGSerializer(serializers.ModelSerializer):
    class Meta:
        model = ONG
        fields = ['id', 'nome', 'endereco', 'contato', 'created_at']



class AnimalSerializer(serializers.ModelSerializer):
    ong_nome = serializers.CharField(source="ong.nome", read_only=True)

    class Meta:
        model = Animal
        fields = [
            'id', 
            'nome', 
            'idade', 
            'especie', 
            'adotado', 
            'ong',        
            'ong_nome',
            'adotante',
            'adotante_nome',    
        ]
        #ocultar o campo ong que mostra só o ID nas respostas de leitura
        extra_kwargs = {
            'ong': {'write_only': True} 
        }

class ConsultaVeterinariaSerializer(serializers.ModelSerializer):
    animal_nome = serializers.CharField(source="animal.nome", read_only=True)

    class Meta:
        model = ConsultaVeterinaria
        fields = [
            'id', 
            'data', 
            'veterinario', 
            'observacoes', 
            'animal',       
            'animal_nome'   
        ]
        extra_kwargs = {
            'animal': {'write_only': True}
        }
        
class AdotanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adotante
        fields = [
            'id', 
            'nome', 
            'cpf', 
            'endereco', 
            'email', 
            'telefone', 
            'created_at'
            ]