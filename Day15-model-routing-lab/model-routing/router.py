from routing_table import MODEL_ROUTING


def select_model(task):

    task = task.lower()

    if task in MODEL_ROUTING:
        return MODEL_ROUTING[task]

    return None