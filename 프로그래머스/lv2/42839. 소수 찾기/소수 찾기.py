from itertools import permutations

def solution(numbers):
    def get_combinations(numbers):
        combinations = []
        for i in range(1, len(numbers) + 1):
            perms = permutations(numbers, i)
            combinations += [int(''.join(perm)) for perm in perms]
        return combinations

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    combinations = get_combinations(numbers)
    prime_count = 0
    for num in set(combinations):  # 중복 조합 제거를 위해 set 사용
        if is_prime(num):
            prime_count += 1
    return prime_count
