import random

# Full Enneagram wing prevalence for all 16 MBTI types
enneagram_wing_prevalence = {
    "INTJ": {
        "1w9": 65, "1w2": 15, "2w1": 0, "2w3": 0,
        "3w2": 6, "3w4": 52, "4w3": 8, "4w5": 19,
        "5w4": 93, "5w6": 116, "6w5": 29, "6w7": 1,
        "7w6": 0, "7w8": 0, "8w7": 23, "8w9": 67,
        "9w8": 3, "9w1": 3
    },
    "ENTJ": {
        "1w9": 12, "1w2": 17, "2w1": 0, "2w3": 1,
        "3w2": 55, "3w4": 127, "4w3": 2, "4w5": 1,
        "5w4": 3, "5w6": 11, "6w5": 7, "6w7": 5,
        "7w6": 2, "7w8": 12, "8w7": 154, "8w9": 91,
        "9w8": 0, "9w1": 0
    },
    "INFJ": {
        "1w9": 64, "1w2": 48, "2w1": 26, "2w3": 11,
        "3w2": 7, "3w4": 6, "4w3": 24, "4w5": 64,
        "5w4": 53, "5w6": 27, "6w5": 56, "6w7": 10,
        "7w6": 1, "7w8": 1, "8w7": 3, "8w9": 3,
        "9w8": 15, "9w1": 81
    },
    "ENFJ": {
        "1w9": 6, "1w2": 37, "2w1": 76, "2w3": 103,
        "3w2": 87, "3w4": 24, "4w3": 21, "4w5": 3,
        "5w4": 1, "5w6": 1, "6w5": 5, "6w7": 29,
        "7w6": 22, "7w8": 15, "8w7": 9, "8w9": 15,
        "9w8": 17, "9w1": 29
    },
    "INTP": {
        "1w9": 8, "1w2": 3, "2w1": 1, "2w3": 0,
        "3w2": 1, "3w4": 6, "4w3": 6, "4w5": 17,
        "5w4": 163, "5w6": 140, "6w5": 44, "6w7": 12,
        "7w6": 8, "7w8": 2, "8w7": 3, "8w9": 3,
        "9w8": 46, "9w1": 37
    },
    "ENTP": {
        "1w9": 0, "1w2": 1, "2w1": 0, "2w3": 2,
        "3w2": 28, "3w4": 28, "4w3": 3, "4w5": 5,
        "5w4": 32, "5w6": 24, "6w5": 7, "6w7": 29,
        "7w6": 121, "7w8": 163, "8w7": 40, "8w9": 2,
        "9w8": 12, "9w1": 3
    },
    "INFP": {
        "1w9": 2, "1w2": 1, "2w1": 15, "2w3": 8,
        "3w2": 1, "3w4": 1, "4w3": 58, "4w5": 137,
        "5w4": 15, "5w6": 7, "6w5": 49, "6w7": 23,
        "7w6": 2, "7w8": 0, "8w7": 0, "8w9": 2,
        "9w8": 30, "9w1": 149
    },
    "ENFP": {
        "1w9": 1, "1w2": 0, "2w1": 8, "2w3": 33,
        "3w2": 12, "3w4": 12, "4w3": 72, "4w5": 11,
        "5w4": 3, "5w6": 1, "6w5": 5, "6w7": 47,
        "7w6": 194, "7w8": 55, "8w7": 14, "8w9": 1,
        "9w8": 13, "9w1": 18
    },
    "ISTJ": {
        "1w9": 152, "1w2": 75, "2w1": 0, "2w3": 1,
        "3w2": 6, "3w4": 14, "4w3": 5, "4w5": 1,
        "5w4": 6, "5w6": 44, "6w5": 137, "6w7": 6,
        "7w6": 0, "7w8": 0, "8w7": 6, "8w9": 26,
        "9w8": 10, "9w1": 11
    },
    "ESTJ": {
        "1w9": 30, "1w2": 88, "2w1": 4, "2w3": 3,
        "3w2": 46, "3w4": 87, "4w3": 1, "4w5": 0,
        "5w4": 1, "5w6": 6, "6w5": 26, "6w7": 22,
        "7w6": 1, "7w8": 6, "8w7": 108, "8w9": 69,
        "9w8": 2, "9w1": 0
    },
    "ISFJ": {
        "1w9": 20, "1w2": 40, "2w1": 97, "2w3": 24,
        "3w2": 5, "3w4": 3, "4w3": 1, "4w5": 4,
        "5w4": 2, "5w6": 2, "6w5": 80, "6w7": 47,
        "7w6": 0, "7w8": 1, "8w7": 0, "8w9": 1,
        "9w8": 17, "9w1": 156
    },
    "ESFJ": {
        "1w9": 1, "1w2": 20, "2w1": 120, "2w3": 131,
        "3w2": 80, "3w4": 15, "4w3": 4, "4w5": 0,
        "5w4": 0, "5w6": 0, "6w5": 4, "6w7": 54,
        "7w6": 25, "7w8": 5, "8w7": 2, "8w9": 4,
        "9w8": 2, "9w1": 33
    },
    "ISTP": {
        "1w9": 3, "1w2": 0, "2w1": 0, "2w3": 0,
        "3w2": 3, "3w4": 15, "4w3": 1, "4w5": 3,
        "5w4": 16, "5w6": 39, "6w5": 78, "6w7": 25,
        "7w6": 2, "7w8": 24, "8w7": 46, "8w9": 100,
        "9w8": 137, "9w1": 8
    },
    "ESTP": {
        "1w9": 1, "1w2": 0, "2w1": 0, "2w3": 1,
        "3w2": 32, "3w4": 32, "4w3": 3, "4w5": 0,
        "5w4": 0, "5w6": 2, "6w5": 1, "6w7": 22,
        "7w6": 32, "7w8": 197, "8w7": 143, "8w9": 21,
        "9w8": 12, "9w1": 1
    },
    "ISFP": {
        "1w9": 4, "1w2": 3, "2w1": 9, "2w3": 6,
        "3w2": 4, "3w4": 15, "4w3": 80, "4w5": 55,
        "5w4": 1, "5w6": 1, "6w5": 39, "6w7": 79,
        "7w6": 9, "7w8": 5, "8w7": 9, "8w9": 14,
        "9w8": 98, "9w1": 69
    },
    "ESFP": {
        "1w9": 0, "1w2": 0, "2w1": 0, "2w3": 29,
        "3w2": 47, "3w4": 39, "4w3": 20, "4w5": 1,
        "5w4": 0, "5w6": 0, "6w5": 0, "6w7": 49,
        "7w6": 154, "7w8": 111, "8w7": 32, "8w9": 5,
        "9w8": 13, "9w1": 0
    }
}

# Instinctual variants
instinctual_variants = ["sp", "so", "sx"]
# Gender options
genders = ["M", "F"]

# Weighted random choice
def weighted_random_choice(choices):
    total = sum(choices.values())
    rand_val = random.uniform(0, total)
    cumulative = 0
    for key, weight in choices.items():
        cumulative += weight
        if rand_val <= cumulative:
            return key
    return None

# Generate valid Tritype
def generate_valid_tritype(mbti, main_enneagram):
    """Generate a valid Tritype with strict rules."""
    gut_triads = {1, 8, 9}
    heart_triads = {2, 3, 4}
    head_triads = {5, 6, 7}
    main_enneagram_number = int(main_enneagram[0])

    if main_enneagram_number in gut_triads:
        valid_triads = [heart_triads, head_triads]
    elif main_enneagram_number in heart_triads:
        valid_triads = [gut_triads, head_triads]
    else:
        valid_triads = [gut_triads, heart_triads]

    alternative_wings = {main_enneagram_number - 1, main_enneagram_number + 1}
    potential_types = enneagram_wing_prevalence[mbti]
    second_candidates = {
        k: v for k, v in potential_types.items()
        if int(k[0]) in valid_triads[0] and int(k[0]) not in alternative_wings
    }
    third_candidates = {
        k: v for k, v in potential_types.items()
        if int(k[0]) in valid_triads[1] and int(k[0]) not in alternative_wings
    }
    second = weighted_random_choice(second_candidates)
    third = weighted_random_choice(third_candidates)
    return [main_enneagram, second, third]

# Generate MBTI profile
def generate_mbti_profile(gender=None):
    mbti = random.choice(list(enneagram_wing_prevalence.keys()))
    main_enneagram = weighted_random_choice(enneagram_wing_prevalence[mbti])
    instinct_primary = random.choice(instinctual_variants)
    instinct_secondary = random.choice([v for v in instinctual_variants if v != instinct_primary])
    if gender is None:
        gender = random.choice(genders)
    tritype = generate_valid_tritype(mbti, main_enneagram)
    tritype_formatted = " ".join(tritype)
    return f"{gender} {mbti} {main_enneagram} {instinct_primary}/{instinct_secondary} {tritype_formatted}"

# Generate and print profiles
profiles = [generate_mbti_profile() for _ in range(1)]
for profile in profiles:
    print(profile)
