from django.db import models
import uuid

class BaseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

# BaseModel com Soft Delete e Manager customizado
class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    # 2. Associe o manager ao modelo
    objects = BaseManager() # O manager padrão agora só retorna ativos
    all_objects = models.Manager() # Um manager que retorna TODOS os objetos

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        self.is_active = False
        self.save()

# ... Seus outros modelos (ONG, Animal, ConsultaVeterinaria) ficam exatamente como estão ...
# Eles herdarão automaticamente os novos managers!

# Modelo ONG
class ONG(BaseModel):
    # ... (sem alterações)
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    contato = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Animal(BaseModel):
    ESPECIES_CHOICES = [
        ("cachorro", "Cachorro"),
        ("gato", "Gato"),
        ("outro", "Outro"),
    ]

    nome = models.CharField(max_length=100)
    idade = models.IntegerField()
    especie = models.CharField(max_length=20, choices=ESPECIES_CHOICES)
    adotado = models.BooleanField(default=False)
    ong = models.ForeignKey(ONG, on_delete=models.CASCADE, related_name="animais")

    adotante = models.ForeignKey(
        'Adotante',
        on_delete=models.SET_NULL,  
        null=True,                   
        blank=True,                  
        related_name='animais'
    )

    def __str__(self):
        return f"{self.nome} ({self.especie})"
    
    class Meta:
        verbose_name = "Animal"
        verbose_name_plural = "Animais"


# Modelo Consulta Veterinária
class ConsultaVeterinaria(BaseModel):
    # ... (sem alterações)
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE, related_name="consultas")
    data = models.DateTimeField()
    veterinario = models.CharField(max_length=100)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Consulta de {self.animal.nome} em {self.data.strftime('%d/%m/%Y %H:%M')}"
    
class Adotante(BaseModel):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(unique=True)  
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome