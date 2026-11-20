from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Главная страница портала мониторинга"""
    context = {
        'title': 'Главная InfraMonitor',
	'message': 'Добро пожаловать в систему мониторинга ИТ-инфраструктуры',
    }
    return render(request, 'monitoring/index.html', context)


def about(request):
    """Страница с информацией о проекте"""
    context = {
	'title': 'О проекте InfraMonitor',
	'message': 'Веб-портал для централизованного мониторинга серверов на базе Zabbix и Prometheus.',
    }
    return render(request, 'monitoring/about.html', context)


def nodes_list(request):
    """Страница со списком все отслеживаемых узлов"""    
    nodes = [
        {'hostname': 'monitor', 'ip': '192.168.56.11', 'status': 'UP'},
        {'hostname': 'node-web', 'ip': '192.168.56.12', 'status': 'UP'},
        {'hostname': 'node-file', 'ip': '192.168.56.13', 'status': 'DOWN'},
    ]
    context = {
        'title': 'Узлы мониторинга',
        'nodes': nodes,
    }
    return render(request, 'monitoring/nodes_list.html', context)


def contacts(request):
    """Страница с формой обратной связи."""
    context = {
        'title': 'Контакты - InfraMonitor',
    }
    return render(request, 'monitoring/contacts.html', context)


def health_check(request):
    """Страница для проверки, что Django работает"""
    return HttpResponse('<h1>InfraMonitor работает!</h1><p>Время сервера: OK</p>')
