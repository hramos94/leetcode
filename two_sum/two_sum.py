def twoSum(nums: list, target: int):
    num_map = {}
    for i, num in enumerate(nums):
        # Calcular o complemento necessário para atingir o alvo
        complement = target - num

        # Verificar se o complemento está no dicionário
        if complement in num_map:
            # Se estiver, retornar os índices dos dois números
            return [num_map[complement], i]

        # Se o complemento não estiver no dicionário, adicionar o número atual ao dicionário
        num_map[num] = i
    # Se nenhum par de números for encontrado, retornar uma lista vazia
    return []


if __name__ == "__main__":
    nums1 = [3, 2, 4]
    nums2 = [150,24,79,50,88,345,3]
    nums3 = [3, 3]
    nums4 = [-10, -1, -18, -19]
    nums5 = [-5, 2, 4, -2, 7]
    nums6 = [-11, -2, -18, -20]
    nums7 = [-1,-2,-3,-4,-5]
    nums8 = [0, 4, 3, 0]
    target1 = 6
    target2 = 200
    target3 = 6
    target4 = -19
    target5 = -7
    target6 = -29
    target7 = -8
    target8 = 0
    a = twoSum(nums4, target4)
    print(a)
