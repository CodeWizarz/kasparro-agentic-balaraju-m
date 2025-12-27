MAX_RETRIES = 2

def with_retry(agent_fn):
    def wrapper(state):
        last_error = None

        for attempt in range(MAX_RETRIES + 1):
            try:
                return agent_fn(state)
            except Exception as e:
                last_error = e
                state["retry_count"] += 1
                state["errors"].append(str(e))

        raise RuntimeError(
            f"Agent {agent_fn.__name__} failed after retries: {last_error}"
        )

    return wrapper
