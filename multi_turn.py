import boto3

def multi_turn_conversation():
    bedrock_runtime = boto3.client('bedrock-runtime', region_name='us-east-1')
    model_id = "us.amazon.nova-lite-v1:0"

    # Sistema de prompt para configurar el comportamiento del asistente
    system_prompt = [
        {
            "text": "Eres un asistente de cocina útil. Proporciona sugerencias de recetas concisas."
        }
    ]   

    # Historial de conversación - lo construiremos con cada turno
    conversation_history = []

    print("DEMO de Conversación Multi-Turno")
    print("=" * 60)

    # Turno 1: Usuario pregunta por sugerencias de recetas
    print("\nTurno 1: Usuario pregunta por sugerencias de recetas.")
    print("-" * 60)

    user_message_1 = "Sugiere una receta rápida para la cena con pollo."  
    print(f"Usuario: {user_message_1}")

    # Agrega el mensaje del usuario al historial antes de llamar a la API
    conversation_history.append({
        "role": "user",
        "content": [{"text": user_message_1}]
    })

    try:
        response_1 = bedrock_runtime.converse(
            modelId=model_id,
            system=system_prompt,
            messages=conversation_history,
            inferenceConfig={"temperature": 0.7, "maxTokens": 200}
        )

        assistant_message_1 = response_1['output']['message']['content'][0]['text']
        print(f"Agente: {assistant_message_1}")

        # Agrega la respuesta del asistente al historial para el siguiente turno
        conversation_history.append({
            "role": "assistant",
            "content": [{"text": assistant_message_1}]
        })

    except Exception as e:
        print(f"Error: {e}")
        return

    # Turno 2: Usuario pregunta por modificaciones
    print("\n\nTurno 2: Usuario pregunta por modificaciones")
    print("-" * 60)

    user_message_2 = "Puedes hacerlo vegetariano en su lugar?"
    print(f"Usuario: {user_message_2}")

    # Agrega el mensaje del usuario al historial antes de llamar a la API
    conversation_history.append({
        "role": "user",
        "content": [{"text": user_message_2}]
    })

    try:
        response_2 = bedrock_runtime.converse(
            modelId=model_id,
            system=system_prompt,
            messages=conversation_history,
            inferenceConfig={"temperature": 0.7, "maxTokens": 200}
        )

        assistant_message_2 = response_2['output']['message']['content'][0]['text']
        print(f"Agente: {assistant_message_2}")

        # Agrega la respuesta del asistente al historial para el siguiente turno
        conversation_history.append({
            "role": "assistant",
            "content": [{"text": assistant_message_2}]
        })

    except Exception as e:
        print(f"Error: {e}")
        return

    #Turno 3: Usuario pregunta por el tiempo de preparación
    print("\n\nTurno 3: Usuario pregunta por el tiempo de preparación")
    print("-" * 60)

    user_message_3 = "¿Cuánto tiempo tomará preparar esto?"
    print(f"Usuario: {user_message_3}")
    
    # Agrega el mensaje del usuario al historial antes de llamar a la API
    conversation_history.append({
        "role": "user",
        "content": [{"text": user_message_3}]
    })

    try:
        response_3 = bedrock_runtime.converse(
            modelId=model_id,
            system=system_prompt,
            messages=conversation_history,
            inferenceConfig={"temperature": 0.7, "maxTokens": 200}
        )

        assistant_message_3 = response_3['output']['message']['content'][0]['text']
        print(f"Agente: {assistant_message_3}")

        # Muestra el uso de tokens para el último turno, que incluye toda la historia de la conversación
        usage = response_3.get('usage', {})
        print(f"\n***FINAL*** Uso de Token:")
        print(f"  Input tokens: {usage.get('inputTokens', 'N/A')} (incluye historial completo)")
        print(f"  Output tokens: {usage.get('outputTokens', 'N/A')}")

    except Exception as e:
        print(f"Error: {e}")
        return

    print("\n" + "=" * 60)
    print(" Nota: Cada llamada a la API incluye el historial completo de la conversación, lo que permite al modelo mantener el contexto a lo largo de múltiples turnos.")

if __name__ == "__main__":
    multi_turn_conversation()