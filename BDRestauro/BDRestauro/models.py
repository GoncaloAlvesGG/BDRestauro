from django.db import models
class Utilizador(models.Model):
    id_utilizador = models.CharField()
    primeiro_nome = models.CharField(max_length=30)
    ultimo_nome = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Consider using a HashField for security
    morada = models.CharField(max_length=128)
    admin = models.BooleanField(default=False)
    telemovel = models.CharField(max_length=14)
    nif = models.CharField(max_length=9, blank=True, null=True)

    def __str__(self):
        return f"{self.primeiro_nome} {self.ultimo_nome}"

""" 

from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Modelo(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.marca})"

class Veiculo(models.Model):
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.modelo}"

class TipoMaoDeObra(models.Model):
    nome = models.CharField(max_length=255)
    custo_hora = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome

class VeiculoUtilizador(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    utilizador = models.ForeignKey(Utilizador, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.veiculo} - {self.utilizador}"

class Estado(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Restauro(models.Model):
    veiculo_utilizador = models.ForeignKey(VeiculoUtilizador, on_delete=models.CASCADE)
    descricao = models.TextField()
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField(blank=True, null=True)
    horas_totais = models.IntegerField(default=0)
    tipo_mao_de_obra = models.ForeignKey(TipoMaoDeObra, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return f"Restauro de {self.veiculo_utilizador} - {self.data_inicio}

"""
