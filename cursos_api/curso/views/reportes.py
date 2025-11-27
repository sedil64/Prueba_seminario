from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["POST"])
def horas_semanales(request):
    horas = request.data.get("horasPorDia", [])

    total = 0
    for h in horas:
        total += h

    promedio = total / 7

    if promedio < 1:
        mensaje = "estudias muy poco"
    elif promedio <= 3:
        mensaje = "Buen ritmo de estudio"
    else:
        mensaje = "Excelente "

    return Response({
        "totalHoras": total,
        "promedio": round(promedio, 2),
        "mensaje": mensaje
    })
