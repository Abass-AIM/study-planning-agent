class PlanningPolicy: # Keep the session-length rule separate from the planning algorithm.
    MAX_SESSION_HOURS = 2.0 # One planned study session may last at most two hours.

    def session_hours(self, estimated_hours: float) -> float: # Decide one session's duration.
        if estimated_hours < 0: # A negative effort estimate is invalid.
            raise ValueError("Estimated hours must not be negative") # Explain the invalid input.
        return min(estimated_hours, self.MAX_SESSION_HOURS) # Cap long estimates; keep short ones.