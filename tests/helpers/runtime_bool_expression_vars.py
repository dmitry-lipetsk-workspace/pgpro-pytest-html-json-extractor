# //////////////////////////////////////////////////////////////////////////////
from .runtime_bool_expression import RuntimeBoolExpression
from . import utils

# //////////////////////////////////////////////////////////////////////////////


class RuntimeBoolExpressionVars:
    class tagExprVar_VERSION(RuntimeBoolExpression.tagExprVar):
        m_item: str

        def __init__(self, value: str):
            assert type(value) is str
            assert value != ""
            self.m_value = value
            return

        # -------------------------------------------------
        def __eq__(self, value: object) -> bool:
            assert type(value) is str
            return utils.compare_version_prefix(self.m_value, value) == 0

        # -------------------------------------------------
        def __ne__(self, value: object) -> bool:
            assert type(value) is str
            return utils.compare_version_prefix(self.m_value, value) != 0

        # -------------------------------------------------
        def __lt__(self, value: object) -> bool:
            assert type(value) is str
            return utils.compare_version_prefix(self.m_value, value) < 0

        # -------------------------------------------------
        def __le__(self, value: object) -> bool:
            assert type(value) is str
            return utils.compare_version_prefix(self.m_value, value) <= 0

        # -------------------------------------------------
        def __gt__(self, value: object) -> bool:
            assert type(value) is str
            return utils.compare_version_prefix(self.m_value, value) > 0

        # -------------------------------------------------
        def __ge__(self, value: object) -> bool:
            assert type(value) is str
            return utils.compare_version_prefix(self.m_value, value) >= 0


# //////////////////////////////////////////////////////////////////////////////
