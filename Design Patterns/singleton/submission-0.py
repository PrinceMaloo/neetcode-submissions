import threading 

class Singleton:
    _instance_lock = threading.Lock()
    _unique_instance = None

    # In python consider this method as the 'getInstance'
    def __new__(cls):
        with cls._instance_lock:
            if cls._unique_instance is None:
                cls._unique_instance = super().__new__(cls)

        return cls._unique_instance

    def getValue(self) -> str:
        return self.value

    def setValue(self, value: str):
        self.value = value
