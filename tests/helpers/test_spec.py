from __future__ import annotations

from .runtime_bool_expression import RuntimeBoolExpression
from .runtime_bool_expression_vars import RuntimeBoolExpressionVars

import typing
import pytest_html

# //////////////////////////////////////////////////////////////////////////////


class TestSpec:
    sm_params: typing.Dict[str, RuntimeBoolExpression.tagExprVar] = {
        "PYTEST_HTML": RuntimeBoolExpressionVars.tagExprVar_VERSION(
            pytest_html.__version__
        ),
    }

    @staticmethod
    def can_run(expression: typing.Optional[str]) -> bool:
        if expression is None:
            return True

        if not expression.strip():
            raise RuntimeError("Expresion is empty.")

        res = RuntimeBoolExpression.eval(expression, __class__.sm_params)
        assert type(res) is bool
        return res


# //////////////////////////////////////////////////////////////////////////////
