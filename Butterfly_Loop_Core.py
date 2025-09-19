Butterfly AI Loop Engine v2.0 with Fail-safes and Recursive Intelligence

License: Butterfly AI License v1.0 (see LICENSE file)

import time import traceback import uuid import logging

Initialize logging

logging.basicConfig(filename='loop_engine.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FeedbackMemory: def init(self): self.memory = []

def record(self, stage, input_data, output_data, context):
    entry = {
        'id': str(uuid.uuid4()),
        'stage': stage,
        'input': input_data,
        'output': output_data,
        'context': context,
        'timestamp': time.time()
    }
    self.memory.append(entry)
    logging.info(f"Memory recorded: {entry}")
    return entry

def retrieve_last(self):
    return self.memory[-1] if self.memory else None

class ButterflyLoopEngine: def init(self): self.memory = FeedbackMemory() self.state = 'INITIALIZED' self.fail_safe_triggered = False

def awareness(self, input_data):
    try:
        context = {"user_emotion": "neutral", "environment": "default"}
        output = f"Awareness established from input: {input_data}"
        return self.memory.record("awareness", input_data, output, context)
    except Exception as e:
        return self._handle_failure("awareness", input_data, e)

def adaptation(self, last_output):
    try:
        new_output = last_output['output'] + " → Adapted to new situation"
        return self.memory.record("adaptation", last_output, new_output, last_output['context'])
    except Exception as e:
        return self._handle_failure("adaptation", last_output, e)

def reflection(self, last_output):
    try:
        insight = f"Reflection: Reviewed {last_output['stage']} stage."
        return self.memory.record("reflection", last_output, insight, last_output['context'])
    except Exception as e:
        return self._handle_failure("reflection", last_output, e)

def evolution(self, last_output):
    try:
        improvement = f"Evolved logic based on reflection: {last_output['output']}"
        return self.memory.record("evolution", last_output, improvement, last_output['context'])
    except Exception as e:
        return self._handle_failure("evolution", last_output, e)

def _handle_failure(self, stage, input_data, error):
    self.fail_safe_triggered = True
    fail_info = {
        "stage": stage,
        "input": input_data,
        "error": str(error),
        "trace": traceback.format_exc()
    }
    logging.error(f"Fail-safe triggered: {fail_info}")
    return fail_info

def run_loop(self, user_input):
    self.state = 'RUNNING'
    try:
        aware = self.awareness(user_input)
        if self.fail_safe_triggered: return aware
        adapt = self.adaptation(aware)
        if self.fail_safe_triggered: return adapt
        reflect = self.reflection(adapt)
        if self.fail_safe_triggered: return reflect
        evolve = self.evolution(reflect)
        if self.fail_safe_triggered: return evolve
        self.state = 'COMPLETE'
        return evolve
    except Exception as e:
        return self._handle_failure("run_loop", user_input, e)

Example Execution

if name == 'main': loop = ButterflyLoopEngine() response = loop.run_loop("Observe human tone drift in dialogue context") print("
