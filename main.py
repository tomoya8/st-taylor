#  Copyright (c) 2025 by Tomoya Konishi
#  All rights reserved.
#
#  License:
#  This program is permitted under the principle of "NO WARRANTY" and
#  "NO RESPONSIBILITY". The author shall not be liable for any event
#  arising in any way out of the use of these resources.
#
#  Redistribution in source and binary forms, with or without
#  modification, is also permitted provided that the above copyright
#  notice, disclaimer and this condition are retained.

import streamlit as st
import sympy as sp
from spb import plot

# https://home.hirosaki-u.ac.jp/relativity/理工系の数学b/sympy-で理工系の数学b/sympy-でテイラー展開・オイラーの公式/
# https://watlab-blog.com/2020/05/05/sympy-taylor-series/

def main():
    st.set_page_config(
        page_title="テイラー展開の可視化",
        page_icon=":chart_with_upwards_trend:",
        layout="wide",
        initial_sidebar_state="auto",
        menu_items={
            'About': "## テーラー展開の可視化📈\n"
                     "Copyright (c) 2025 by Tomoya Konishi. All rights reserved."
        }
    )

    st.title("テイラー展開の可視化")

    fx = st.sidebar.text_input("関数 $f(x) = $", "x * cos(x)")
    n = st.sidebar.number_input("テイラー展開の次数 $n = $", min_value=1, max_value=20, value=5, step=1)
    a = st.sidebar.number_input("展開中心 $a$ = ", value=0.0, step=0.1)
    if a != 0:
        st.sidebar.warning("展開中心が$a\\ne0$の場合、展開が正しくおこなわれない場合があります。", icon="⚠️")

    sp.init_printing(order="rev-lex")
    x = sp.Symbol("x")
    expr = sp.sympify(fx)
    taylor = expr.series(x, a, n+1)

    st.write("もとの関数:　$f(x)=" + sp.latex(expr) + "$")
    if a != 0:
        rounded_taylor = round_expr(taylor, 3)
        st.write("テイラー展開: $\\displaystyle\\bar{f}(x)=" + sp.latex(rounded_taylor) + "$")
        st.warning("展開中心が $a\\ne0$ の場合、数値を四捨五入しています。")
    else:
        st.write("テイラー展開: $\\displaystyle\\bar{f}(x)=" + sp.latex(taylor) + "$")

    p = plot(
        (expr, f"${sp.latex(expr)}$"),
        (taylor.removeO(), "Taylor"),
        (x, -10, 10),
        markers=[{'args': [a, expr.subs({x: a}), 'ro'], 'ms': 5}],
        ylim=(-10, 10),
        show=False
    )
    st.pyplot(p.fig)


def round_expr(expr, num_digits):
    """
    Rounds all numerical terms in a SymPy expression to a specified number of digits.
    """
    return expr.xreplace({n: round(n, num_digits) for n in expr.atoms(sp.Number)})

if __name__ == "__main__":
    main()