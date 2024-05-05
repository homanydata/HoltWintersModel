def linear_interpolation(data: list[float]) -> list[float]:
    result = []
    for i, n in enumerate(data):
        if isinstance(n, int | float):
            result.append(n)
        else:
            if i == 0 or i == len(data) - 1:
                raise ValueError("first or last value cannot be null")
            prev_index, prev = len(result) - 1, result[-1]
            next_index, next = [(j+i+1, x) for j, x in enumerate(data[i+1:]) if x is not None][0]
            value = prev + (next - prev) / (next_index - prev_index) * (i - prev_index)
            result.append(value)
    return result


d = [0, None, 10, None, None, 40]
print(linear_interpolation(d))
