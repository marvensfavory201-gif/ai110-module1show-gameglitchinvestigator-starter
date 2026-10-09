from logic_utils import check_guess, update_score

def test_winning_guess():
    # check_guess returns a tuple: (outcome, message)
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"

# --- NEW TESTS TARGETING THE FIXED BUGS ---

def test_update_score_penalizes_too_high_even_attempts():
    """Verify that a 'Too High' guess on an even attempt correctly deducts 5 points (fixes the exploit)."""
    current_score = 100
    # Attempt 2 is an even attempt number
    new_score = update_score(current_score, outcome="Too High", attempt_number=2)
    assert new_score == 95  # Should be 95, not 105

def test_update_score_penalizes_too_high_odd_attempts():
    """Verify that a 'Too High' guess on an odd attempt correctly deducts 5 points."""
    current_score = 100
    new_score = update_score(current_score, outcome="Too High", attempt_number=1)
    assert new_score == 95

def test_update_score_penalizes_too_low():
    """Verify that a 'Too Low' guess correctly deducts 5 points."""
    current_score = 100
    new_score = update_score(current_score, outcome="Too Low", attempt_number=1)
    assert new_score == 95
