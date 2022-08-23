## Ejercicio 1

El equipo esta construyendo un sistema que genera una lista de tareas pendientes (ToDo List). Usando Django se definió la clase Todo en el Modelo:

~~~
  class Todo(models.Model):
      task = models.CharField(max_length = 180)
      timestamp = models.DateTimeField(auto_now_add = True, auto_now = False, blank = True)
      completed = models.BooleanField(default = False, blank = True)
      updated = models.DateTimeField(auto_now = True, blank = True)
    
      def __str__(self):
          return self.task
~~~

Se requiere generar una API que cree una nueva tarea, que modifique el estado de una tarea a completado, que permita ver el detalle de una tarea y que obtenga una lista de todas las tareas pendientes.

## Ejercicio 2

Una consultora de desarrollo tiene un sistema que guarda información sobre los programadores del equipo. La consultora es parte de un conjunto de empresas donde comparten información entre sí.

El sistema esta desarrollado en DJANGO y tienen definido el siguiente modelo

~~~
  LANG_CHOICES = (
  ("js", "Javascript"),
  ('python', 'Python'),
  ('c', 'C'),
  ('java', 'Java'),
  ('php', 'PHP')
  )

  class Programmer(models.Model):

  nick = models.CharField(max_length=16)

  first_name = models.CharField(max_length=255)

  last_name = models.CharField(max_length=255)

  email = models.EmailField()

  program_lang = models.CharField(max_length=32, choices=LANG_CHOICES)

~~~

Se requiere desarrollar una API con las siguiente funcionalidades:

Dado un lenguaje determinado, obtener todos los programadores
Crear varios programadores a la vez
Ver los detalles de un programador

## Ejercicio 3

Se esta contruyendo un sistema de ecommerce en django. Una de las aplicaciones que esta desarrollando el equipo el carrito de compras. Para tal fin se definio el siguiente modelo:

~~~
class CartItem(models.Model):

 product_name = models.CharField(max_length=200)

 product_price = models.FloatField()

 product_quantity = models.PositiveIntegerField()
~~~
Se pide crear una API con las operaciones estandar para un item del carrito, usando ViewSets y Routers

## Ejercicio 4

Se desarrollo el siguiente código para gestionar operaciones CRUD de una base de datos de héroes.

Modelo
~~~
class HeroSerializer(serializers.HyperlinkedModelSerializer):

 class Meta:

 model = Hero

 fields = ('name', 'alias')
~~~
Vista
~~~
class HeroViewSet(viewsets.ModelViewSet):

 queryset = Hero.objects.all().order_by('name')

 serializer_class = HeroSerializer

URL

urlpatterns = [

 path('admin/', admin.site.urls),

 path('', include('myapi.urls')),

 ]
~~~
Para utilizar esta API se requiere establecer permisos donde solo los usuarios registrados puedan utilizarla, adicionalmente solo se puede permitir hacer un update al usuario que lo creo.