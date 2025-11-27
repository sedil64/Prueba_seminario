from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def aprobacion(request):
    notas = request.data.get("notas", [])
    nota_minima = request.data.get("notaMinima", 7)

    total = 0
    for nota in notas:
        total += nota

    promedio = total / len(notas)

    if promedio >= nota_minima:
        estado = "Aprobado"
        mensaje = "El estudiante ha aprobado"
    else:
        estado = "Reprobado"
        mensaje = "El estudiante no ha aprobado"

    return Response({
        "promedio": round(promedio, 2),
        "estado": estado,
        "mensaje": mensaje
    })
