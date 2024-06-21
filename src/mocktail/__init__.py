from mocktail.factory import Factory


def mocktail(model_class: type, quantity: int):
    print("------1")
    print(model_class)

    return Factory().make(model_class, quantity=quantity)
