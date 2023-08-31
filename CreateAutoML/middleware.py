import reflex as rx


class LoggingMiddleware(rx.Middleware):
    def preprocess(self, app, state, event):
        print(f"Middleware preprocess Event {event}")

    def postprocess(self, app, state, event, update):
        print(f"Middleware postprocess Update {update}")