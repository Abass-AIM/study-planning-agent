from abc import ABC, abstractmethod  # Import abstract-base-class helpers so persistence can be described as a contract. 

class StudyRepository(ABC):  # Define the persistence operations needed by the Study Planning Agent use case. 

    @abstractmethod  # Require concrete repositories to persist a student. 

    def save_student(self, student):  # Declare persistence for the STUDENTS relation. 

        raise NotImplementedError  # Prevent the port from choosing a database technology. 

    @abstractmethod  # Require concrete repositories to persist assignments. 

    def save_assignments(self, student_id, assignments):  # Declare persistence for ASSIGNMENTS and its student foreign key. 

        raise NotImplementedError  # Prevent the port from choosing a database technology. 

    @abstractmethod  # Require concrete repositories to create a persistent planning request. 

    def create_request(self, student_id):  # Declare creation of one PLANNING_REQUESTS row. 

        raise NotImplementedError  # Prevent the port from choosing a database technology. 

    @abstractmethod  # Require concrete repositories to persist request state transitions. 

    def update_request_state(self, request_id, state):  # Declare task-state persistence for a planning request. 

        raise NotImplementedError  # Prevent the port from choosing a database technology. 

    @abstractmethod  # Require concrete repositories to persist tool-call logs. 

    def log_tool_call(self, request_id, tool_name, status, details):  # Declare trace/log persistence for one external tool call. 

        raise NotImplementedError  # Prevent the port from choosing a database technology. 

    @abstractmethod  # Require concrete repositories to persist the generated plan aggregate. 

    def save_plan(self, plan):  # Declare relational persistence for STUDY_PLANS and PLAN_ITEMS. 

        raise NotImplementedError  # Prevent the port from choosing a database technology. 