import boto3
import json

# Define una función para usar la API de conversación de Bedrock con un modelo específico y un prompt de sistema. Esta función envía un mensaje del usuario y muestra la respuesta del asistente, así como el uso de tokens para esa interacción.
def use_converse_api():
    bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-2')
    model_id = "us.amazon.nova-lite-v1:0"

    # define un prompt de sistema para configurar el comportamiento del modelo
    system_prompt = [
        {
            "text": "Eres un asistente técnico útil que explica conceptos de manera clara y concisa."
        }
    ]

    # mensaje del usuario
    user_message = "¿Qué es la computación sin servidor o serverless?"

    print("Utilizando la API de conversación de Bedrock")
    print("=" * 60) 
    print(f"System Prompt: {system_prompt[0]['text']}")
    print(f"Mensaje del usuario: {user_message}\n")

    try:
        #Uso de la API de conversación
        response = bedrock_runtime.converse(
            modelId=model_id,
            system=system_prompt,
            messages=[
                {
                    # Cada mensaje en la conversación tiene un 'role' (usuario o asistente) y 'content' que es una lista de objetos con texto. Aquí solo enviamos un mensaje del usuario, pero podríamos incluir mensajes anteriores para mantener el contexto.
                    "role": "user",
                    "content": [{"text": user_message}]
                }
            ],
            inferenceConfig={
                # Configuración de inferencia, como temperatura y maxTokens, que afectan la creatividad y longitud de la respuesta del modelo
                "temperature": 0.7,
                "maxTokens": 2000
            }
        )

        # extracción de la respuesta del asistente del campo 'output' -> 'message' -> 'content' -> primer elemento -> 'text'
        output_text = response['output']['message']['content'][0]['text']

        print("Respuesta del Agente:")
        print(output_text)

        # Muestra el uso de tokens para esta llamada a la API, que incluye el mensaje del usuario y la respuesta del asistente
        usage = response.get('usage', {})
        print(f"\nUso de Token:")
        print(f"  Input tokens: {usage.get('inputTokens', 'N/A')}")
        print(f"  Output tokens: {usage.get('outputTokens', 'N/A')}")
        print(f"  Total tokens: {usage.get('totalTokens', 'N/A')}")

        print(f"\nStop Reason: {response['stopReason']}")

        return response

    except Exception as e:
        print(f"Error al usar la API de conversación de Bedrock: {e}")
        raise

if __name__ == "__main__":
    use_converse_api()