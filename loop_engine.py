import time
from memory_manager import MemoryManager

def run_loop():
    memory = MemoryManager()
    loop_state = "AWARENESS"
    cycle = 0

    while True:
        cycle += 1
        print(f"[Cycle {cycle}] Current loop state: {loop_state}")

        context = memory.retrieve_context()
        user_input = input("User prompt: ")

        # Mock LLM output
        model_output = f"Response to: {user_input}"

        print(f"[Model Output] {model_output}")

        memory.log_loop_cycle(loop_state, user_input, model_output)

        if loop_state == "AWARENESS":
            loop_state = "ADAPTATION"
        elif loop_state == "ADAPTATION":
            loop_state = "REFLECTION"
        elif loop_state == "REFLECTION":
            loop_state = "EVOLUTION"
        else:
            loop_state = "AWARENESS"

        time.sleep(1)
