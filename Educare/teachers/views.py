from django.shortcuts import render
from django.http import JsonResponse
from .models import Marks

def student_performance_chart(request):
    # Querying and processing data to generate chart
    # Example: Grouping by year and calculating average performance
    data = {
        'labels': ['Year 1', 'Year 2', 'Year 3', 'Year 4'],
        'datasets': [
            {
                'label': 'Average Performance',
                'data': [80, 75, 85, 90],  # Replace with actual data retrieval logic
                'backgroundColor': 'rgba(54, 162, 235, 0.2)',
                'borderColor': 'rgba(54, 162, 235, 1)',
                'borderWidth': 1,
            },
        ]
    }

    return JsonResponse(data)
