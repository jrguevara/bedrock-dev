# Amazon Bedrock para principiantes

Este repositorio contiene ejemplos de código que te llevarán desde tu primera llamada a la API de Bedrock hasta un agente de IA completamente funcional. Al final, construirás un chatbot de preguntas  que utiliza una base de conocimientos RAG, guardrails para seguridad de contenido,  y el SDK de Strands Agents para unirlo todo.

## Prerequisitos

- Python 3.12+
- Una cuenta de AWS con [credenciales configuradas localmente](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)
- ***Nota:*** Necesitarás crear un rol o usuario IAM en tu cuenta para seguir el tutorial, no puedes completarlo usando el usuario root.

## Paso 1: Instalar boto3
Instala el SDK de AWS para Python:

```bash
pip install boto3
```
## Paso 2: Instalar dependencias

Crear un entorno virtual e instalar los paquetes requeridos:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requerimientos.txt
```

## Project Structure

```
├── converse_api.py               # API de conversación + mensajes del sistema
├── multi_turn.py                 # Conversación de múltiples turnos
├── requirements.txt
└── README.md
```

## Ejecutar los ejemplos

Trabaja a través de estos en orden. Cada uno se basa en conceptos del anterior.

## 1. Converse API — Tu primera llamada a la API

```bash
python3 bedrock-examples/converse_api.py
```

Realiza una llamada a Amazon Nova Lite usando la API de conversación. Demuestra los mensajes del sistema, el formato de los mensajes y los parámetros de inferencia (temperatura, maxTokens) y el uso de tokens.

## 2. Conversaciones de múltiples turnos

```bash
python3 bedrock-examples/multi_turn.py
```

Es una conversación de 3 turnos con un asistente de cocina. Muestra cómo mantener el historial de la conversación manualmente, ya que los modelos son sin estado: cada llamada a la API necesita que se vuelva a enviar todo el historial.

## Recursos

- [Amazon Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)
- [Bedrock Supported Models & IDs](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html)
- [Strands Agents SDK](https://strandsagents.com/)
- [Bedrock Pricing](https://aws.amazon.com/bedrock/pricing/)

