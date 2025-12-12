# Alternate US Presidential History Generator

A Python-based generator that creates an alternate history of United States presidents from 1789 to 2024, complete with randomized political parties, personality profiles, and historical events.

## Features

### President Generation
- **Timeline**: Generates presidents from 1789 to 2024
- **Period-Accurate Names**: Names are selected based on historical era (early, mid, late, modern)
- **Gender**: Male presidents until 2000, then 20% chance of female presidents
- **Personality Profiles**: Uses MBTI and Enneagram personality types from the character generator
- **Political Compass**: Each president has social and economic political positions (-100 to +100)
- **Life Details**:
  - Birth and death years based on historical life expectancy by era
  - State of origin (considering state admission dates)
  - Wealth class (from homeless to elite)
- **Terms**: Presidents can serve 1 or 2 terms (65% chance of 2 terms)
- **Deaths in Office**:
  - ~18% chance of dying in office
  - Can die from natural causes or assassination
  - Automatic successor generation from same party
- **Successors**: When a president dies, a successor completes the term with 50% chance of reelection

### Political Party System
- **Formation**: 2-4 parties form in 1792
- **New Parties**: Each election has a 1/x chance of new party forming (x = number of current parties)
- **Political Shifts**: Each party shifts ±20 points on social and economic axes each election
- **Dissolution**: Parties out of power for 20+ years have 33% chance of dissolving each election
- **Color Names**: Parties are named after colors (Red Party, Blue Party, etc.)

### State Eligibility Rules
Presidents can be from:
- Any of the original 13 colonies
- States where they were at least 15 years old when the state was admitted
- States they were born in after admission

### Wealth Distribution
Wealth scores (0-10) are weighted to create realistic distribution:
- 0 (Homeless): 2% chance
- 1-3 (Lower Class): 9% chance
- 4-6 (Middle Class): 26% chance
- 7-9 (Upper Class): 30% chance
- 10 (Elite): 9% chance

## Usage

```bash
python3 alternate_president_generator.py
```

To save the output to a file:

```bash
python3 alternate_president_generator.py > my_alternate_history.txt
```

## Output Format

Each president entry includes:
- Name and gender
- Term years
- Political party
- Death in office (if applicable)
- Political position (social and economic scores)
- Life span
- State of origin
- Wealth class and score
- Personality profile (MBTI, Enneagram, etc.)

### Example Output

```
================================================================================
President: Benjamin Hamilton (Male)
Term: 1789-1797
Party: No Party
Number of Terms: 2 terms
Political Position: Social +63, Economic +29
Life: 1742-1814 (72 years)
State of Origin: South Carolina
Wealth: Lower Class (Score: 2/10)
Personality: M ENTJ 8w7 sp/so 8w7 3w2 6w7
================================================================================
```

## Summary Statistics

At the end of each simulation, you'll see:
- Total presidents generated
- Total parties formed (and how many are still active)
- Number of deaths in office (by cause)
- Number of female presidents
- List of active parties with their current political positions

## Files

- `alternate_president_generator.py` - Main generator program
- `character_generator.py` - Personality profile generator using MBTI and Enneagram
- `README.md` - This file

## Requirements

- Python 3.x
- No external dependencies required

## How It Works

1. **First President (1789)**: Generated without a party affiliation
2. **Party Formation (1792)**: 2-4 political parties are created with random ideologies
3. **Election Cycles**: Every 4 or 8 years (based on term length), a new president is elected from a random active party
4. **Dynamic Party System**: Parties shift ideologically, new parties form, old parties dissolve
5. **Historical Progression**: Continues until reaching the 2024 election

Each run creates a completely unique alternate history!

## License

This project is open source and available for educational and entertainment purposes.
