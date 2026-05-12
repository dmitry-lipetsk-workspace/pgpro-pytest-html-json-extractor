# //////////////////////////////////////////////////////////////////////////////
import typing

# //////////////////////////////////////////////////////////////////////////////


def parse_version_string(ver_str: str) -> typing.List[int]:
    if not isinstance(ver_str, str):
        raise TypeError(
            "Expected string, got {0}: {1!r}".format(
                type(ver_str).__name__,
                ver_str,
            )
        )

    if not ver_str:
        raise ValueError("Version string is empty")

    segments = ver_str.split(".")
    result = []

    for i, segment in enumerate(segments):
        if not segment:
            raise ValueError(
                "Empty segment found at index {0} in version string: {1!r}".format(  # noqa: E501
                    i,
                    ver_str,
                )
            )

        if not segment.isdigit():
            raise ValueError(
                "Invalid version segment {0!r} at index {1} in string: {2!r}".format(  # noqa: E501
                    segment,
                    i,
                    ver_str,
                )
            )

        result.append(int(segment))
        continue

    assert len(result) > 0
    return result


# ------------------------------------------------------------------------
def compare_version_prefix(ver: str, prefix: str) -> int:
    assert type(ver) is str
    assert type(prefix) is str

    v_parts = parse_version_string(ver)
    assert type(v_parts) is list
    assert len(v_parts) > 0
    p_parts = parse_version_string(prefix)
    assert type(p_parts) is list
    assert len(p_parts) > 0
    return compare_version_prefix_t(v_parts, p_parts)


# ------------------------------------------------------------------------
def compare_version_prefix_t(ver: typing.List[int], prefix: typing.List[int]) -> int:
    assert type(ver) is list
    assert len(ver) > 0
    assert type(prefix) is list
    assert len(prefix) > 0

    idx_v = 0
    idx_p = 0

    n_v = len(ver)
    n_p = len(prefix)

    while True:
        if idx_p == n_p:
            return 0

        if idx_v == n_v:
            while True:
                if idx_p == n_p:
                    return 0

                assert type(prefix[idx_p]) is int
                if prefix[idx_p] != 0:
                    return -1
                idx_p += 1

        assert type(ver[idx_v]) is int
        assert type(prefix[idx_p]) is int

        if ver[idx_v] < prefix[idx_p]:
            return -1

        if prefix[idx_p] < ver[idx_v]:
            return 1

        idx_v += 1
        idx_p += 1
        continue


# //////////////////////////////////////////////////////////////////////////////
