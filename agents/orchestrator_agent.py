class OrchestratorAgent:
    def run(self, pipeline: list):
        context = {}
        for step in pipeline:
            context.update(step(context))
        return context
