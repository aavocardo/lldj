def precision(prediction, target) -> float:

    prediction_: list = prediction
    target_: list = target
    deviation: list = []
    result_: list = []
    _result: list = []

    def average(arg) -> int:
        total = sum(arg)
        avg = total/len(arg)
        return avg

    for i in range(len(prediction_)):
        if prediction_[i] <= target_[i]:
            temp = str(target_[i] - prediction_[i])
            deviation.append(f'±{temp}')
        else:
            if prediction_[i] >= target_[i]:
                temp = str(prediction_[i] - target_[i])
                deviation.append(f'±{temp}')

    for j in range(len(prediction_)):
        precision_ = str(int(abs((((target_[j]-prediction_[j])/target_[j])*100)-100)))
        _result.append(f'{precision_}%')
        result_.append(int(precision_))

    average_precision: int = round(average(result_))
    print(f'Precision = {average_precision}%')

    print('\nPrediction:')
    print(*prediction_, sep=' - ')

    print('\nTarget:')
    print(*target_, sep=' - ')

    # print('\nDeviation:')
    # print(*deviation, sep=' - ')

    # final.append(f'{average_precision}%')
    final = average_precision/100
    # final.extend(deviation)

    return final
