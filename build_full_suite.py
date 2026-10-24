# -*- coding: utf-8 -*-
"""
Master Compiler for Course Study Guide & Interactive Webpage (v2.0)
Statistical Learning for Reliability Analysis (Lectures 1–60)
Prof. Monalisa Sarma (IIT Kharagpur)
"""

import os, sys, re, json

def build_study_guide():
    print("Assembling study_guide.md...")
    modules = []
    for i in range(1, 13):
        fname = f"modules/mod{i:02d}.md"
        if os.path.exists(fname):
            with open(fname, "r", encoding="utf-8") as f:
                modules.append(f.read().strip())
        else:
            print(f"Warning: {fname} not found!")

    header = """# STATISTICAL LEARNING FOR RELIABILITY ANALYSIS
## Complete Comprehensive Course Study Guide & Reference Handbook
**Instructor:** Prof. Monalisa Sarma | *Subir Chowdhury School of Quality and Reliability, IIT Kharagpur*  
**Course Code:** NPTEL / SWAYAM | **Coverage:** Complete Curriculum (Lectures 01 – 60)

---

> [!NOTE]
> **About this Master Study Guide:**  
> This comprehensive study guide provides an exhaustive, mathematically rigorous, and pedagogically structured synthesis of the complete 60-lecture curriculum. It includes all formal definitions, Kolmogorov axioms, probability theorems, sampling distributions, inferential testing catalogs, ANOVA decompositions, regression equations, time-series forecasting, and machine learning classifiers (Naive Bayes, $k$-NN, Support Vector Machines & Kernel Methods). For every topic, it details **Problem Types Commonly Solved**, trigger keywords, step-by-step solution algorithms, and worked numerical tutorial examples directly from the course transcripts.

---

## TABLE OF CONTENTS
1. [Module 1: Foundations of Reliability Engineering & Statistical Thinking (Lectures 01–02)](#module-1-foundations-of-reliability-engineering--statistical-thinking-lectures-0102)
2. [Module 2: Probability Theory, Set Operations & System Reliability Modeling (Lectures 03–06)](#module-2-probability-theory-set-operations--system-reliability-modeling-lectures-0306)
3. [Module 3: Discrete Probability Distributions & Reliability Applications (Lectures 07–11)](#module-3-discrete-probability-distributions--reliability-applications-lectures-0711)
4. [Module 4: Continuous Probability Distributions & Hazard Rate Modeling (Lectures 12–15)](#module-4-continuous-probability-distributions--hazard-rate-modeling-lectures-1215)
5. [Module 5: Sampling Distributions & The Central Limit Theorem (Lectures 16–21)](#module-5-sampling-distributions--the-central-limit-theorem-lectures-1621)
6. [Module 6: Statistical Inference — Point Estimation & Confidence Intervals (Lectures 26–28)](#module-6-statistical-inference--point-estimation--confidence-intervals-lectures-2628)
7. [Module 7: Statistical Inference — Hypothesis Testing & Goodness-of-Fit (Lectures 22–25, 29–31)](#module-7-statistical-inference--hypothesis-testing--goodness-of-fit-lectures-2225-2931)
8. [Module 8: Analysis of Variance (ANOVA) (Lectures 32–37)](#module-8-analysis-of-variance-anova-lectures-3237)
9. [Module 9: Correlation & Linear Regression Analysis (Lectures 38–43)](#module-9-correlation--linear-regression-analysis-lectures-3843)
10. [Module 10: Auto-Regression & Time-Series Modeling for Reliability (Lecture 44)](#module-10-auto-regression--time-series-modeling-for-reliability-lecture-44)
11. [Module 11: Logistic Regression & Binary Classification (Lectures 45–48)](#module-11-logistic-regression--binary-classification-lectures-4548)
12. [Module 12: Machine Learning Classifiers: Bayes, k-NN & Support Vector Machines (Lectures 49–60)](#module-12-machine-learning-classifiers-bayes-k-nn--support-vector-machines-lectures-4960)

---
"""

    full_md = header + "\n\n" + "\n\n---\n\n".join(modules)
    with open("study_guide.md", "w", encoding="utf-8") as f_out:
        f_out.write(full_md)
    print(f"study_guide.md successfully created ({len(full_md)} characters).")


def convert_md_to_html_content(md_text):
    """
    Robust Markdown to HTML converter with Math Protection.
    Extracts math tokens BEFORE any HTML transformations to prevent formula corruption.
    """
    math_blocks = []
    math_inlines = []

    # Step 1: Protect display math $$...$$
    def save_block_math(match):
        idx = len(math_blocks)
        content = match.group(1).strip()
        # Clean potential dangerous HTML tags inside math
        content = content.replace("<", "&lt;").replace(">", "&gt;")
        math_blocks.append(content)
        return f"@@MATH_BLOCK_{idx}@@"

    text = re.sub(r'\$\$(.*?)\$\$', save_block_math, md_text, flags=re.DOTALL)

    # Step 2: Protect inline math $...$
    def save_inline_math(match):
        idx = len(math_inlines)
        content = match.group(1).strip()
        content = content.replace("<", "&lt;").replace(">", "&gt;")
        math_inlines.append(content)
        return f"@@MATH_INLINE_{idx}@@"

    text = re.sub(r'(?<!\$)\$(?!\$)([^\$\n]+?)(?<!\$)\$(?!\$)', save_inline_math, text)

    lines = text.split("\n")
    html_lines = []
    in_code_block = False
    in_table = False
    table_rows = []
    in_callout = False
    callout_type = ""
    callout_content = []
    in_ul = False
    in_ol = False

    def close_lists():
        nonlocal in_ul, in_ol
        res = ""
        if in_ul:
            res += "</ul>\n"
            in_ul = False
        if in_ol:
            res += "</ol>\n"
            in_ol = False
        return res

    def flush_table():
        nonlocal in_table, table_rows
        if not table_rows:
            in_table = False
            return ""
        out = '<div class="table-responsive"><table class="custom-table">\n'
        for idx, row in enumerate(table_rows):
            if idx == 0:
                out += '<thead><tr>' + ''.join(f'<th>{c.strip()}</th>' for c in row) + '</tr></thead>\n<tbody>\n'
            else:
                out += '<tr>' + ''.join(f'<td>{c.strip()}</td>' for c in row) + '</tr>\n'
        out += '</tbody></table></div>\n'
        table_rows = []
        in_table = False
        return out

    def flush_callout():
        nonlocal in_callout, callout_type, callout_content
        cls = "callout-info"
        icon = "💡"
        title = "KEY CONCEPT"
        if callout_type == "NOTE":
            cls = "callout-note"
            icon = "📌"
            title = "FORMULA & CONCEPT REFERENCE"
        elif callout_type == "WARNING":
            cls = "callout-warning"
            icon = "⚠️"
            title = "COMMON PITFALL & DISTINCTION"
        elif callout_type == "IMPORTANT":
            cls = "callout-important"
            icon = "⭐"
            title = "CRITICAL THEOREM & INSIGHT"
        elif callout_type == "CAUTION":
            cls = "callout-caution"
            icon = "🛑"
            title = "CAUTION & GOTCHA"

        body = "<br>".join([parse_inline_formatting(line) for line in callout_content if line.strip()])
        out = f'<div class="callout-card {cls}"><div class="callout-header"><span class="callout-icon">{icon}</span> <strong>{title}</strong></div><div class="callout-body">{body}</div></div>\n'
        in_callout = False
        callout_type = ""
        callout_content = []
        return out

    def parse_inline_formatting(txt):
        # Format bold, italics, inline code safely
        txt = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', txt)
        txt = re.sub(r'\*(.*?)\*', r'<em>\1</em>', txt)
        txt = re.sub(r'`([^`]+)`', r'<code>\1</code>', txt)
        return txt

    i = 0
    # Extract module title if first line is # MODULE
    if lines and lines[0].startswith("# MODULE "):
        mod_title = parse_inline_formatting(lines[0][2:].strip())
        mod_id = re.sub(r'[^a-zA-Z0-9_-]+', '-', mod_title.lower()).strip('-')
        html_lines.append(f'<section id="{mod_id}" class="module-section card">')
        html_lines.append(f'<h2 class="module-title">{mod_title}</h2>')
        i = 1

    while i < len(lines):
        line = lines[i]

        # Code block
        if line.startswith("```"):
            html_lines.append(close_lists())
            if in_code_block:
                html_lines.append("</code></pre></div>")
                in_code_block = False
            else:
                lang = line[3:].strip() or "text"
                html_lines.append(f'<div class="code-container"><pre><code class="language-{lang}">')
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            html_lines.append(escaped)
            i += 1
            continue

        # Callouts
        if line.startswith("> [!"):
            html_lines.append(close_lists())
            m = re.match(r'> \[!(NOTE|WARNING|IMPORTANT|CAUTION|TIP)\]', line)
            if m:
                if in_callout:
                    html_lines.append(flush_callout())
                in_callout = True
                callout_type = m.group(1)
                callout_content = []
                i += 1
                continue

        if in_callout:
            if line.startswith(">"):
                callout_content.append(line[1:].strip())
                i += 1
                continue
            else:
                html_lines.append(flush_callout())

        # Tables
        if "|" in line and (line.strip().startswith("|") or line.strip().endswith("|")):
            html_lines.append(close_lists())
            parts = [p.strip() for p in line.strip().split("|")[1:-1]]
            if all(re.match(r'^:?-+:?$', p) for p in parts if p):
                i += 1
                continue
            if not in_table:
                in_table = True
                table_rows = []
            table_rows.append([parse_inline_formatting(p) for p in parts])
            i += 1
            continue
        elif in_table:
            html_lines.append(flush_table())

        # Step-by-Step Worked Problems (Collapsible Accordion)
        if line.startswith("### Problem "):
            html_lines.append(close_lists())
            problem_title = line[4:].strip()
            problem_body = []
            i += 1
            while i < len(lines) and not lines[i].startswith("### ") and not lines[i].startswith("## ") and not lines[i].startswith("# ") and not lines[i].startswith("---"):
                problem_body.append(lines[i])
                i += 1
            
            p_text = "\n".join(problem_body)
            if "**Solution:**" in p_text or "**Solution**" in p_text:
                parts = re.split(r'\*\*Solution:?\*\*', p_text, maxsplit=1)
                stmt = parts[0].strip()
                sol = parts[1].strip() if len(parts) > 1 else ""
            else:
                stmt = p_text
                sol = ""

            def render_problem_text(txt):
                """Inline formatting plus pipe tables (tables would otherwise print as raw markdown)."""
                chunks, buf, rows = [], [], []

                def flush_buf():
                    if buf:
                        chunks.append(parse_inline_formatting("\n".join(buf)).replace("\n\n", "<br><br>").replace("\n- ", "<br>• "))
                        buf.clear()

                def flush_rows():
                    if rows:
                        out = '<div class="table-responsive"><table class="custom-table">\n<thead><tr>' + ''.join(f'<th>{c}</th>' for c in rows[0]) + '</tr></thead>\n<tbody>\n'
                        out += ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>\n' for r in rows[1:])
                        chunks.append(out + '</tbody></table></div>\n')
                        rows.clear()

                for ln in txt.split("\n"):
                    if ln.strip().startswith("|") and ln.strip().endswith("|"):
                        flush_buf()
                        parts = [c.strip() for c in ln.strip().split("|")[1:-1]]
                        if all(re.match(r'^:?-+:?$', c) for c in parts if c):
                            continue
                        rows.append([parse_inline_formatting(c) for c in parts])
                    else:
                        flush_rows()
                        buf.append(ln)
                flush_rows()
                flush_buf()
                return "".join(chunks)

            stmt_html = render_problem_text(stmt)
            sol_html = render_problem_text(sol)

            card_html = f'''
            <div class="problem-card">
                <div class="problem-header">
                    <span class="problem-badge">WORKED EXAMPLE</span>
                    <h4 class="problem-title">{parse_inline_formatting(problem_title)}</h4>
                </div>
                <div class="problem-statement">
                    {stmt_html}
                </div>
                <details class="solution-details">
                    <summary class="solution-toggle">
                        <span class="toggle-icon">🔍</span> <strong>Reveal Step-by-Step Solution &amp; Derivations</strong>
                    </summary>
                    <div class="solution-content">
                        {sol_html}
                    </div>
                </details>
            </div>
            '''
            html_lines.append(card_html)
            continue

        # Headings
        if line.startswith("## "):
            html_lines.append(close_lists())
            h2_text = parse_inline_formatting(line[3:].strip())
            h2_id = re.sub(r'[^a-zA-Z0-9_-]+', '-', h2_text.lower()).strip('-')
            html_lines.append(f'<h3 id="{h2_id}" class="section-h2">{h2_text}</h3>')
            i += 1
            continue
        elif line.startswith("### "):
            html_lines.append(close_lists())
            h3_text = parse_inline_formatting(line[4:].strip())
            html_lines.append(f'<h4 class="section-h3">{h3_text}</h4>')
            i += 1
            continue
        elif line.startswith("#### "):
            html_lines.append(close_lists())
            h4_text = parse_inline_formatting(line[5:].strip())
            html_lines.append(f'<h5 class="section-h4">{h4_text}</h5>')
            i += 1
            continue

        # Horizontal Rules
        if line.strip() in ["---", "***", "___"]:
            html_lines.append(close_lists())
            html_lines.append('<hr class="section-divider">')
            i += 1
            continue

        # Blockquotes
        if line.startswith("> "):
            html_lines.append(close_lists())
            bq_text = parse_inline_formatting(line[2:].strip())
            html_lines.append(f'<blockquote class="custom-quote">{bq_text}</blockquote>')
            i += 1
            continue

        # Lists (Unordered)
        if line.strip().startswith("- ") or line.strip().startswith("* "):
            if in_ol:
                html_lines.append("</ol>\n")
                in_ol = False
            if not in_ul:
                html_lines.append('<ul class="custom-list">\n')
                in_ul = True
            item_text = parse_inline_formatting(line.strip()[2:])
            html_lines.append(f'<li class="list-item">{item_text}</li>')
            i += 1
            continue

        # Lists (Ordered)
        m_num = re.match(r'^\s*(\d+)\.\s+(.*)', line)
        if m_num:
            if in_ul:
                html_lines.append("</ul>\n")
                in_ul = False
            if not in_ol:
                html_lines.append('<ol class="custom-ol">\n')
                in_ol = True
            item_text = parse_inline_formatting(m_num.group(2))
            html_lines.append(f'<li class="list-item-num" value="{m_num.group(1)}">{item_text}</li>')
            i += 1
            continue

        # Paragraph
        if line.strip():
            html_lines.append(close_lists())
            p_text = parse_inline_formatting(line.strip())
            html_lines.append(f'<p class="body-p">{p_text}</p>')

        i += 1

    html_lines.append(close_lists())
    if in_table:
        html_lines.append(flush_table())
    if in_callout:
        html_lines.append(flush_callout())
    if in_code_block:
        html_lines.append("</code></pre></div>")

    html_lines.append("</section>")

    full_html = "\n".join(html_lines)

    # Step 3: Re-insert protected math tokens
    for idx, content in enumerate(math_blocks):
        # Wrap display math cleanly in div
        token = f"@@MATH_BLOCK_{idx}@@"
        replacement = f'<div class="math-display-wrap">$$\n{content}\n$$</div>'
        full_html = full_html.replace(token, replacement)

    for idx, content in enumerate(math_inlines):
        # Wrap inline math cleanly in span
        token = f"@@MATH_INLINE_{idx}@@"
        replacement = f'<span class="math-inline">${content}$</span>'
        full_html = full_html.replace(token, replacement)

    return full_html


def build_interactive_html():
    print("Building index.html with Bright Peach Theme, Complete Cheat Sheet Hub, and Safe MathJax...")
    
    # Read modules
    modules_md = []
    module_nav = []
    for i in range(1, 13):
        fname = f"modules/mod{i:02d}.md"
        with open(fname, "r", encoding="utf-8") as f:
            raw_text = f.read().strip()
            first_line = raw_text.split("\n")[0].replace("# MODULE ", "Module ")
            mod_id = re.sub(r'[^a-zA-Z0-9_-]+', '-', first_line.lower()).strip('-')
            modules_md.append(raw_text)
            module_nav.append((mod_id, first_line))

    # Convert modules to HTML
    rendered_modules = []
    for raw in modules_md:
        rendered_modules.append(convert_md_to_html_content(raw))

    all_modules_html = "\n\n".join(rendered_modules)
    nav_links_html = "".join(f'<a href="#{nav[0]}">{nav[1]}</a>\n' for nav in module_nav)

    # Generate Cheat Sheet Cards for all 12 modules
    cheat_sheet_cards = r"""
    <!-- Category 1: Reliability & Hazard Functions -->
    <div class="cheat-card" data-cat="rel">
        <div class="cheat-cat-badge">Reliability Foundations</div>
        <h4 class="cheat-title">Reliability &amp; Hazard Rate Fundamental Equations</h4>
        <div class="cheat-formula">$$R(t) = P(T &gt; t) = \exp\left(-\int_0^t h(u)du\right)$$</div>
        <div class="cheat-formula">$$h(t) = \frac{f(t)}{R(t)} = -\frac{d}{dt}\ln R(t), \quad \text{MTTF} = \int_0^\infty R(t) dt$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Converting between hazard function $h(t)$, PDF $f(t)$, CDF $F(t)$, and reliability $R(t)$; finding MTTF from survival curves.
        </div>
    </div>

    <!-- Category 2: System Reliability -->
    <div class="cheat-card" data-cat="sys">
        <div class="cheat-cat-badge">System Reliability</div>
        <h4 class="cheat-title">Series, Parallel &amp; $k$-out-of-$n$ Active Redundancy</h4>
        <div class="cheat-formula">$$R_{\text{series}} = \prod_{i=1}^n R_i, \quad R_{\text{parallel}} = 1 - \prod_{i=1}^n(1 - R_i)$$</div>
        <div class="cheat-formula">$$R_{k/n} = \sum_{i=k}^n \binom{n}{i} R^i (1-R)^{n-i}$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Weakest-link series systems; active parallel redundancy; multi-engine aircraft survival; majority voting gates.
        </div>
    </div>

    <!-- Category 3: Bayes' Theorem -->
    <div class="cheat-card" data-cat="bayes">
        <div class="cheat-cat-badge">Probability &amp; Bayes</div>
        <h4 class="cheat-title">Bayes' Theorem &amp; Total Probability</h4>
        <div class="cheat-formula">$$P(B_j \mid A) = \frac{P(A \mid B_j) P(B_j)}{\sum_{i=1}^k P(A \mid B_i) P(B_i)}$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Multi-factory defect attribution; medical test false-positive rates; sensor diagnostic symptom updating.
        </div>
    </div>

    <!-- Category 4: Discrete Distributions -->
    <div class="cheat-card" data-cat="disc">
        <div class="cheat-cat-badge">Discrete Distributions</div>
        <h4 class="cheat-title">Binomial, Poisson &amp; Geometric Models</h4>
        <div class="cheat-formula">$$\text{Binomial: } P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$$</div>
        <div class="cheat-formula">$$\text{Poisson: } P(X=k) = \frac{e^{-\lambda}\lambda^k}{k!}, \quad \text{Geometric: } P(X&gt;k)=(1-p)^k$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Lot acceptance testing; rare defect density per wafer/PCB; trials until first component breakdown.
        </div>
    </div>

    <!-- Category 5: Continuous Distributions -->
    <div class="cheat-card" data-cat="cont">
        <div class="cheat-cat-badge">Continuous Distributions</div>
        <h4 class="cheat-title">Exponential, Normal &amp; Weibull Distributions</h4>
        <div class="cheat-formula">$$\text{Exponential: } R(t) = e^{-\lambda t}, \quad \text{MTTF} = 1/\lambda$$</div>
        <div class="cheat-formula">$$\text{Weibull: } R(t) = \exp\left[ -(t/\theta)^\beta \right], \quad h(t) = \frac{\beta}{\theta}(t/\theta)^{\beta-1}$$</div>
        <div class="cheat-formula">$$\text{Tolerance Clearance: } C = X_2 - X_1 \sim N(\mu_2 - \mu_1, \sigma_1^2 + \sigma_2^2)$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Constant failure rate mission times; shaft-bearing interference probability; Weibull infant ($\beta&lt;1$) vs wearout ($\beta&gt;1$) modeling.
        </div>
    </div>

    <!-- Category 6: Sampling & Central Limit Theorem -->
    <div class="cheat-card" data-cat="samp">
        <div class="cheat-cat-badge">Sampling &amp; CLT</div>
        <h4 class="cheat-title">Sample Mean &amp; Variance Distributions</h4>
        <div class="cheat-formula">$$Z = \frac{\bar{X} - \mu}{\sigma/\sqrt{n}} \sim N(0, 1), \quad \chi^2 = \frac{(n-1)S^2}{\sigma^2} \sim \chi^2(n-1)$$</div>
        <div class="cheat-formula">$$F = \frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2} \sim F(n_1-1, n_2-1)$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Evaluating sample average probabilities for large samples ($n \ge 30$); sample variance compliance tests; comparing two machine variances.
        </div>
    </div>

    <!-- Category 7: Estimation & Confidence Intervals -->
    <div class="cheat-card" data-cat="est">
        <div class="cheat-cat-badge">Inference &amp; CIs</div>
        <h4 class="cheat-title">Confidence Intervals for $\mu, \sigma^2, p$</h4>
        <div class="cheat-formula">$$\text{Mean (Small } n): \bar{x} \pm t_{\alpha/2, n-1}\left(\frac{s}{\sqrt{n}}\right)$$</div>
        <div class="cheat-formula">$$\text{Variance: } \left[ \frac{(n-1)s^2}{\chi^2_{\alpha/2, n-1}}, \frac{(n-1)s^2}{\chi^2_{1-\alpha/2, n-1}} \right]$$</div>
        <div class="cheat-formula">$$\text{Sample Size: } n = \left(\frac{Z_{\alpha/2}\sigma}{E}\right)^2$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Small-sample prototype lifespan bounds; non-symmetric variance bounds; determining sample size for target error margin.
        </div>
    </div>

    <!-- Category 8: Hypothesis Testing & Contingency Tables -->
    <div class="cheat-card" data-cat="hyp">
        <div class="cheat-cat-badge">Hypothesis Testing</div>
        <h4 class="cheat-title">One-Sample Tests &amp; Chi-Square Independence</h4>
        <div class="cheat-formula">$$t = \frac{\bar{x} - \mu_0}{s/\sqrt{n}} \sim t(n-1), \quad \chi^2 = \sum \frac{(O - E)^2}{E} \sim \chi^2((r-1)(c-1))$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Battery lifespan specification verification; distribution goodness-of-fit; testing independence between failure mode and manufacturing shift.
        </div>
    </div>

    <!-- Category 9: Analysis of Variance (ANOVA) -->
    <div class="cheat-card" data-cat="anova">
        <div class="cheat-cat-badge">ANOVA</div>
        <h4 class="cheat-title">One-Way ANOVA &amp; Tukey's HSD Post-Hoc</h4>
        <div class="cheat-formula">$$SST = SSB + SSW, \quad F = \frac{MSB}{MSE} = \frac{SSB/(k-1)}{SSW/(N-k)}$$</div>
        <div class="cheat-formula">$$HSD = q_{\alpha, k, N-k}\sqrt{\frac{MSE}{n}}$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Comparing $k \ge 3$ material/process means simultaneously without Family-Wise Error inflation; pinpointing significantly differing pairs.
        </div>
    </div>

    <!-- Category 10: Linear Regression & Correlation -->
    <div class="cheat-card" data-cat="reg">
        <div class="cheat-cat-badge">Linear Regression</div>
        <h4 class="cheat-title">OLS Regression, Intervals &amp; $R^2$</h4>
        <div class="cheat-formula">$$\hat{\beta}_1 = \frac{S_{xy}}{S_{xx}}, \quad \hat{\beta}_0 = \bar{y} - \hat{\beta}_1\bar{x}, \quad R^2 = \frac{SSR}{SST}$$</div>
        <div class="cheat-formula">$$\text{Pred. Interval: } \hat{y}_0 \pm t_{\alpha/2, n-2} s_e \sqrt{1 + \frac{1}{n} + \frac{(X_0 - \bar{x})^2}{S_{xx}}}$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Degradation rate prediction from temperature; goodness of fit via $R^2$; bounding individual future unit responses.
        </div>
    </div>

    <!-- Category 11: Time Series AR(1) -->
    <div class="cheat-card" data-cat="ts">
        <div class="cheat-cat-badge">Time-Series &amp; AR(1)</div>
        <h4 class="cheat-title">Autoregression &amp; Remaining Useful Life (RUL)</h4>
        <div class="cheat-formula">$$X_t = c + \phi_1 X_{t-1} + a_t, \quad \mu = \frac{c}{1-\phi_1}, \quad \text{Var}(X_t) = \frac{\sigma^2}{1-\phi_1^2}$$</div>
        <div class="cheat-formula">$$\hat{X}_{T+h} = \mu + \phi_1^h(X_T - \mu)$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Sensor vibration telemetry forecasting; stationarity check ($|\phi_1| &lt; 1$); Remaining Useful Life (RUL) estimation before alarm threshold.
        </div>
    </div>

    <!-- Category 12: Logistic Regression -->
    <div class="cheat-card" data-cat="logit">
        <div class="cheat-cat-badge">Logistic Regression</div>
        <h4 class="cheat-title">Logit Link, Odds Ratio &amp; Classification Metrics</h4>
        <div class="cheat-formula">$$\text{logit}(p) = \ln\left(\frac{p}{1-p}\right) = \boldsymbol{\beta}^T\mathbf{x}, \quad p(\mathbf{x}) = \frac{1}{1 + e^{-\boldsymbol{\beta}^T\mathbf{x}}}$$</div>
        <div class="cheat-formula">$$\text{Odds Ratio: } OR_j = e^{\beta_j}, \quad F_1 = \frac{2 \cdot \text{Precision} \cdot \text{Recall}}{\text{Precision} + \text{Recall}}$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Predicting binary breakdown probability from voltage/thermal stresses; odds multiplier interpretation; confusion matrix diagnostics.
        </div>
    </div>

    <!-- Category 13: Support Vector Machines -->
    <div class="cheat-card" data-cat="svm">
        <div class="cheat-cat-badge">Support Vector Machines</div>
        <h4 class="cheat-title">SVM Dual Optimization, Hyperplanes &amp; Kernels</h4>
        <div class="cheat-formula">$$\max_{\boldsymbol{\alpha}} \sum \alpha_i - \frac{1}{2}\sum\sum \alpha_i \alpha_j y_i y_j K(\mathbf{x}_i, \mathbf{x}_j) \quad \text{s.t. } 0 \le \alpha_i \le C, \; \sum \alpha_i y_i = 0$$</div>
        <div class="cheat-formula">$$\mathbf{w} = \sum_{i \in \text{SV}} \alpha_i y_i \mathbf{x}_i, \quad b = y_k - \mathbf{w}^T\mathbf{x}_k, \quad \text{Margin } \gamma = \frac{2}{\|\mathbf{w}\|}$$</div>
        <div class="cheat-formula">$$\text{Gaussian RBF: } K(\mathbf{x}, \mathbf{z}) = \exp\left(-\gamma \|\mathbf{x} - \mathbf{z}\|^2\right)$$</div>
        <div class="cheat-solved">
            <strong>Problems Solved:</strong> Finding optimal separating hyperplanes from 2D coordinate points; identifying Support Vectors ($\alpha_i &gt; 0$); classifying non-linear failure clusters.
        </div>
    </div>
    """

    with open("template_v2.html", "w", encoding="utf-8") as tf:
        tf.write(r'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <script>
    (function(){var t='dark';try{t=localStorage.getItem('theme')||'dark';}catch(e){}document.documentElement.setAttribute('data-theme',t);})();
    </script>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
    <title>Statistical Learning for Reliability Analysis — Course Study Guide &amp; Interactive Master Handbook</title>
    
    <!-- Meta SEO -->
    <meta name="description" content="Comprehensive interactive study guide and lecture notes for Statistical Learning for Reliability Analysis (Lectures 01-60) by Prof. Monalisa Sarma, IIT Kharagpur. Covers Probability, Hazard Modeling, Sampling, Inference, ANOVA, Regression, Logistic Regression, Naive Bayes, k-NN, and SVM.">
    <meta name="keywords" content="Reliability Engineering, Statistical Learning, Probability, Weibull, Sampling Distribution, Hypothesis Testing, ANOVA, Linear Regression, Logistic Regression, Support Vector Machines, Prof. Monalisa Sarma, IIT Kharagpur">
    
    <!-- Google Fonts: Inter & Outfit -->
    <link rel="stylesheet" href="vendor/fonts.css">
    
    <!-- MathJax 3 with LaTeX Configuration -->
    <script>
    window.MathJax = {
        tex: {
            inlineMath: [['$', '$'], ['\\(', '\\)']],
            displayMath: [['$$', '$$'], ['\\[', '\\]']],
            processEscapes: true,
            processEnvironments: true
        },
        options: {
            skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code']
        },
        startup: {
            pageReady: () => {
                return MathJax.startup.defaultPageReady().then(() => {
                    console.log('MathJax initial typesetting complete');
                });
            }
        }
    };
    </script>
    <script id="MathJax-script" async src="vendor/mathjax/es5/tex-mml-chtml.js"></script>

    <style>
        /* ==========================================================================
           BRIGHT PEACH DESIGN SYSTEM & THEME TOKENS
           ========================================================================== */
        :root {
            --bg-body: #FFFDF9;            /* Warm off-white / soft cream */
            --surface-card: #FFFFFF;       /* Pure white card surface */
            --surface-alt: #FFF8F2;        /* Subtle peach tint */
            --accent-peach-light: #FFE0D6; /* Soft peach highlight */
            --accent-peach: #FFAB91;       /* Warm peach primary */
            --accent-peach-vivid: #FF8A65; /* Vibrant peach */
            --accent-terracotta: #FF7043;  /* Bold peach / terracotta */
            --primary-dark: #D84315;       /* Deep burnt orange */
            --text-heading: #3E2723;       /* Deep warm terracotta charcoal */
            --text-body: #37474F;          /* High-legibility slate charcoal */
            --text-muted: #607D8B;         /* Secondary slate text */
            --border-soft: #FFE5D9;        /* Soft peach border */
            --border-medium: #FFCCBC;      /* Medium peach accent border */
            --callout-bg: #FFF3E0;         /* Soft peach callout fill */
            --callout-border: #FF7043;     /* Left callout border */
            --shadow-card: 0 4px 16px rgba(183, 28, 28, 0.04), 0 2px 6px rgba(0, 0, 0, 0.03);
            --shadow-hover: 0 8px 24px rgba(230, 74, 25, 0.12), 0 3px 8px rgba(0, 0, 0, 0.04);
            --font-main: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            --font-heading: 'Outfit', 'Inter', sans-serif;
            --font-mono: 'Fira Code', Consolas, Monaco, monospace;
            --container-width: 920px;
            --header-height: 70px;
            --radius-md: 12px;
            --radius-lg: 18px;
        }

        /* Reset & Base Styles */
        *, *::before, *::after {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html {
            scroll-behavior: smooth;
            font-size: 16px;
        }

        body {
            background-color: var(--bg-body);
            color: var(--text-body);
            font-family: var(--font-main);
            line-height: 1.75;
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            padding-top: var(--header-height);
        }

        /* Scroll Progress Bar */
        #progress-container {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 4px;
            background: rgba(255, 171, 145, 0.2);
            z-index: 1000;
        }
        #progress-bar {
            height: 100%;
            width: 0%;
            background: linear-gradient(90deg, var(--accent-peach), var(--accent-terracotta), var(--primary-dark));
            transition: width 0.1s ease;
        }

        /* Sticky Navigation Header */
        header.sticky-header {
            position: fixed;
            top: 4px;
            left: 0;
            right: 0;
            height: var(--header-height);
            background: rgba(255, 253, 249, 0.95);
            backdrop-filter: blur(12px);
            border-bottom: 1px solid var(--border-soft);
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 0 2rem;
            z-index: 999;
            box-shadow: 0 2px 10px rgba(216, 67, 21, 0.03);
        }

        .header-brand {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            text-decoration: none;
            color: var(--text-heading);
            font-family: var(--font-heading);
            font-weight: 700;
            font-size: 1.15rem;
        }
        .brand-badge {
            background: linear-gradient(135deg, var(--accent-peach-vivid), var(--primary-dark));
            color: #FFFFFF;
            font-size: 0.75rem;
            font-weight: 800;
            padding: 0.2rem 0.6rem;
            border-radius: 20px;
            letter-spacing: 0.5px;
        }

        .header-actions {
            display: flex;
            align-items: center;
            gap: 1rem;
        }

        .search-box {
            position: relative;
            display: flex;
            align-items: center;
        }
        .search-box input {
            background: var(--surface-card);
            border: 1px solid var(--border-medium);
            padding: 0.5rem 1rem 0.5rem 2.2rem;
            border-radius: 30px;
            font-size: 0.88rem;
            color: var(--text-heading);
            outline: none;
            width: 220px;
            transition: all 0.3s ease;
            font-family: var(--font-main);
        }
        .search-box input:focus {
            width: 320px;
            border-color: var(--accent-terracotta);
            box-shadow: 0 0 0 3px rgba(255, 112, 67, 0.15);
        }
        .search-box svg {
            position: absolute;
            left: 0.8rem;
            width: 16px;
            height: 16px;
            fill: var(--text-muted);
        }

        .nav-btn {
            background: var(--surface-alt);
            border: 1px solid var(--border-medium);
            color: var(--text-heading);
            padding: 0.5rem 1rem;
            border-radius: 8px;
            font-weight: 600;
            font-size: 0.85rem;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            transition: all 0.2s ease;
        }
        .nav-btn:hover {
            background: var(--accent-peach);
            color: #FFFFFF;
            border-color: var(--accent-peach-vivid);
        }
        .nav-btn.active-btn {
            background: var(--primary-dark);
            color: #FFFFFF;
            border-color: var(--primary-dark);
        }

        /* Sidebar Navigation Drawer */
        #nav-drawer {
            position: fixed;
            top: calc(var(--header-height) + 4px);
            left: 0;
            bottom: 0;
            width: 320px;
            background: var(--surface-card);
            border-right: 1px solid var(--border-soft);
            overflow-y: auto;
            padding: 1.5rem 1rem;
            transform: translateX(-100%);
            transition: transform 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            z-index: 998;
            box-shadow: 4px 0 20px rgba(0, 0, 0, 0.05);
        }
        #nav-drawer.open {
            transform: translateX(0);
        }
        .drawer-title {
            font-family: var(--font-heading);
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-heading);
            margin-bottom: 1rem;
            padding-left: 0.5rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .drawer-nav {
            display: flex;
            flex-direction: column;
            gap: 0.4rem;
        }
        .drawer-nav a {
            padding: 0.6rem 0.8rem;
            border-radius: 8px;
            font-size: 0.85rem;
            color: var(--text-body);
            text-decoration: none;
            transition: all 0.2s ease;
            font-weight: 500;
            border-left: 3px solid transparent;
        }
        .drawer-nav a:hover, .drawer-nav a.active {
            background: var(--surface-alt);
            color: var(--primary-dark);
            border-left-color: var(--accent-terracotta);
            font-weight: 600;
        }

        /* Hero Banner */
        .hero-banner {
            background: linear-gradient(135deg, #FFF3E0 0%, #FFE0B2 50%, #FFCCBC 100%);
            border-radius: var(--radius-lg);
            padding: 3.5rem 2.5rem;
            margin: 2rem auto;
            max-width: var(--container-width);
            border: 1px solid rgba(255, 171, 145, 0.3);
            box-shadow: var(--shadow-card);
            text-align: center;
            position: relative;
            overflow: hidden;
        }
        .hero-banner::before {
            content: '';
            position: absolute;
            top: -50px;
            right: -50px;
            width: 180px;
            height: 180px;
            background: radial-gradient(circle, rgba(255, 138, 101, 0.25) 0%, transparent 70%);
            border-radius: 50%;
        }
        .hero-tag {
            display: inline-block;
            background: var(--primary-dark);
            color: #FFFFFF;
            font-size: 0.75rem;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            padding: 0.3rem 0.9rem;
            border-radius: 20px;
            margin-bottom: 1.2rem;
        }
        .hero-title {
            font-family: var(--font-heading);
            font-size: 2.3rem;
            font-weight: 800;
            color: var(--text-heading);
            line-height: 1.25;
            margin-bottom: 1rem;
        }
        .hero-subtitle {
            font-size: 1.1rem;
            color: #4E342E;
            max-width: 720px;
            margin: 0 auto 1.8rem;
            font-weight: 400;
        }
        .hero-meta {
            display: flex;
            justify-content: center;
            gap: 2rem;
            font-size: 0.88rem;
            color: #6D4C41;
            font-weight: 600;
            flex-wrap: wrap;
        }
        .meta-pill {
            background: rgba(255, 255, 255, 0.7);
            padding: 0.4rem 1rem;
            border-radius: 30px;
            border: 1px solid rgba(255, 171, 145, 0.4);
        }

        /* Main Container */
        main.main-container {
            max-width: var(--container-width);
            margin: 0 auto;
            padding: 0 1.5rem 4rem;
        }

        /* Module Sections (Cards) */
        section.module-section {
            background: var(--surface-card);
            border-radius: var(--radius-lg);
            padding: 2.8rem 2.2rem;
            margin-bottom: 3rem;
            border: 1px solid var(--border-soft);
            box-shadow: var(--shadow-card);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }
        section.module-section:hover {
            box-shadow: var(--shadow-hover);
        }

        h2.module-title {
            font-family: var(--font-heading);
            font-size: 1.75rem;
            font-weight: 800;
            color: var(--text-heading);
            border-bottom: 3px solid var(--accent-peach);
            padding-bottom: 0.75rem;
            margin-bottom: 2rem;
            position: relative;
        }
        h2.module-title::after {
            content: '';
            position: absolute;
            bottom: -3px;
            left: 0;
            width: 80px;
            height: 3px;
            background: var(--primary-dark);
        }

        h3.section-h2 {
            font-family: var(--font-heading);
            font-size: 1.35rem;
            font-weight: 700;
            color: var(--primary-dark);
            margin-top: 2.2rem;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        h3.section-h2::before {
            content: '§';
            color: var(--accent-peach-vivid);
            font-weight: 800;
        }

        h4.section-h3 {
            font-family: var(--font-heading);
            font-size: 1.12rem;
            font-weight: 600;
            color: var(--text-heading);
            margin-top: 1.6rem;
            margin-bottom: 0.6rem;
        }

        h5.section-h4 {
            font-size: 1rem;
            font-weight: 600;
            color: var(--text-body);
            margin-top: 1.2rem;
            margin-bottom: 0.4rem;
        }

        p.body-p {
            margin-bottom: 1.2rem;
            color: var(--text-body);
            font-size: 1rem;
            line-height: 1.8;
        }

        hr.section-divider {
            border: none;
            height: 1px;
            background: linear-gradient(90deg, transparent, var(--border-medium), transparent);
            margin: 2.2rem 0;
        }

        /* Lists */
        ul.custom-list, ol.custom-ol {
            margin: 1rem 0 1.4rem 1.8rem;
        }
        li.list-item, li.list-item-num {
            margin-bottom: 0.5rem;
            line-height: 1.7;
            color: var(--text-body);
        }

        /* Callout Cards */
        .callout-card {
            border-radius: var(--radius-md);
            padding: 1.4rem 1.6rem;
            margin: 1.8rem 0;
            border-left: 5px solid var(--callout-border);
            background-color: var(--callout-bg);
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
        }
        .callout-header {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            font-family: var(--font-heading);
            font-weight: 700;
            font-size: 0.95rem;
            color: var(--text-heading);
            margin-bottom: 0.6rem;
        }
        .callout-icon {
            font-size: 1.2rem;
        }
        .callout-body {
            font-size: 0.96rem;
            line-height: 1.7;
            color: #424242;
        }
        .callout-note {
            background-color: #FFF3E0;
            border-left-color: #FF7043;
        }
        .callout-warning {
            background-color: #FFF8E1;
            border-left-color: #FFA000;
        }
        .callout-important {
            background-color: #FBE9E7;
            border-left-color: #D84315;
        }
        .callout-caution {
            background-color: #FFEBEE;
            border-left-color: #E53935;
        }

        /* Custom Tables */
        .table-responsive {
            overflow-x: auto;
            margin: 1.8rem 0;
            border-radius: var(--radius-md);
            border: 1px solid var(--border-soft);
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.02);
        }
        table.custom-table {
            width: 100%;
            border-collapse: collapse;
            font-size: 0.92rem;
            background: var(--surface-card);
            text-align: left;
        }
        table.custom-table th {
            background: var(--surface-alt);
            color: var(--text-heading);
            font-family: var(--font-heading);
            font-weight: 700;
            padding: 0.9rem 1.1rem;
            border-bottom: 2px solid var(--border-medium);
        }
        table.custom-table td {
            padding: 0.8rem 1.1rem;
            border-bottom: 1px solid #FFF0E6;
            color: var(--text-body);
        }
        table.custom-table tr:hover td {
            background-color: #FFFDF9;
        }

        /* Code Blocks */
        .code-container {
            background: #2D2424;
            border-radius: var(--radius-md);
            padding: 1.2rem 1.4rem;
            margin: 1.6rem 0;
            overflow-x: auto;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .code-container pre {
            font-family: var(--font-mono);
            font-size: 0.88rem;
            color: #FFE0D6;
            line-height: 1.6;
        }
        code {
            font-family: var(--font-mono);
            font-size: 0.9em;
            background: #FFEBE5;
            color: var(--primary-dark);
            padding: 0.15rem 0.4rem;
            border-radius: 4px;
        }

        /* Math Display Wrappers */
        .math-display-wrap {
            overflow-x: auto;
            margin: 1.2rem 0;
            padding: 0.6rem 0;
            text-align: center;
        }
        .math-inline {
            white-space: nowrap;
        }

        /* Problem & Worked Example Cards */
        .problem-card {
            background: #FFFDFB;
            border: 1px solid var(--border-medium);
            border-radius: var(--radius-md);
            padding: 1.8rem;
            margin: 2.2rem 0;
            box-shadow: 0 3px 10px rgba(255, 112, 67, 0.06);
            border-left: 6px solid var(--accent-peach-vivid);
        }
        .problem-header {
            display: flex;
            align-items: center;
            gap: 0.8rem;
            margin-bottom: 1rem;
            flex-wrap: wrap;
        }
        .problem-badge {
            background: var(--accent-terracotta);
            color: #FFFFFF;
            font-size: 0.72rem;
            font-weight: 800;
            padding: 0.2rem 0.6rem;
            border-radius: 4px;
            letter-spacing: 0.5px;
        }
        .problem-title {
            font-family: var(--font-heading);
            font-size: 1.15rem;
            font-weight: 700;
            color: var(--text-heading);
        }
        .problem-statement {
            font-size: 0.98rem;
            color: var(--text-body);
            margin-bottom: 1.4rem;
            line-height: 1.75;
            background: rgba(255, 243, 224, 0.4);
            padding: 1rem 1.2rem;
            border-radius: 8px;
            border: 1px dashed var(--border-medium);
        }

        /* Interactive Collapsible Solutions */
        .solution-details {
            margin-top: 1rem;
            background: #FFFFFF;
            border: 1px solid var(--border-soft);
            border-radius: 8px;
            overflow: hidden;
            transition: all 0.3s ease;
        }
        .solution-toggle {
            background: var(--surface-alt);
            padding: 0.8rem 1.2rem;
            font-size: 0.92rem;
            color: var(--primary-dark);
            cursor: pointer;
            font-weight: 600;
            display: flex;
            align-items: center;
            gap: 0.5rem;
            user-select: none;
            transition: background 0.2s ease;
        }
        .solution-toggle:hover {
            background: #FFE6DB;
        }
        .solution-content {
            padding: 1.4rem;
            font-size: 0.96rem;
            line-height: 1.8;
            color: var(--text-body);
            background: #FFFFFF;
            border-top: 1px solid var(--border-soft);
        }

        /* ==========================================================================
           COMPREHENSIVE MASTER FORMULA CHEAT SHEET DRAWER / MODAL
           ========================================================================== */
        #cheat-sheet-drawer {
            position: fixed;
            top: 0;
            right: 0;
            bottom: 0;
            width: 620px;
            max-width: 95vw;
            background: #FFFDF9;
            box-shadow: -6px 0 30px rgba(0, 0, 0, 0.18);
            border-left: 2px solid var(--border-medium);
            z-index: 10001;
            transform: translateX(100%);
            transition: transform 0.35s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            flex-direction: column;
        }
        #cheat-sheet-drawer.open {
            transform: translateX(0);
        }
        .drawer-backdrop {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: rgba(46, 26, 21, 0.5);
            backdrop-filter: blur(3px);
            z-index: 10000;
            display: none;
        }
        .drawer-backdrop.show {
            display: block;
        }

        .cheat-header {
            padding: 1.2rem 1.5rem;
            background: linear-gradient(135deg, #FFE0B2, #FFCCBC);
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border-medium);
        }
        .cheat-header-title {
            font-family: var(--font-heading);
            font-weight: 800;
            font-size: 1.2rem;
            color: var(--text-heading);
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        .cheat-close-btn {
            background: none;
            border: none;
            font-size: 1.5rem;
            cursor: pointer;
            color: var(--text-heading);
            font-weight: 700;
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
        }
        .cheat-close-btn:hover {
            background: rgba(255, 255, 255, 0.6);
        }

        .cheat-filter-bar {
            padding: 0.8rem 1.2rem;
            background: var(--surface-alt);
            border-bottom: 1px solid var(--border-soft);
            display: flex;
            gap: 0.5rem;
            flex-wrap: wrap;
        }
        .cheat-tab-btn {
            background: #FFFFFF;
            border: 1px solid var(--border-soft);
            padding: 0.35rem 0.75rem;
            border-radius: 20px;
            font-size: 0.78rem;
            font-weight: 600;
            color: var(--text-body);
            cursor: pointer;
            transition: all 0.2s ease;
        }
        .cheat-tab-btn:hover, .cheat-tab-btn.active {
            background: var(--primary-dark);
            color: #FFFFFF;
            border-color: var(--primary-dark);
        }

        .cheat-search-input {
            width: 100%;
            padding: 0.5rem 1rem;
            border-radius: 6px;
            border: 1px solid var(--border-medium);
            font-size: 0.85rem;
            font-family: var(--font-main);
            outline: none;
            margin-top: 0.4rem;
        }
        .cheat-search-input:focus {
            border-color: var(--accent-terracotta);
            box-shadow: 0 0 0 2px rgba(255, 112, 67, 0.2);
        }

        .cheat-body {
            padding: 1.2rem;
            overflow-y: auto;
            flex: 1;
            display: flex;
            flex-direction: column;
            gap: 1.2rem;
        }

        .cheat-card {
            background: #FFFFFF;
            border: 1px solid var(--border-medium);
            border-radius: var(--radius-md);
            padding: 1.2rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
            border-left: 4px solid var(--accent-terracotta);
            transition: transform 0.2s ease;
        }
        .cheat-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(255, 112, 67, 0.1);
        }
        .cheat-cat-badge {
            display: inline-block;
            font-size: 0.7rem;
            font-weight: 800;
            color: var(--primary-dark);
            text-transform: uppercase;
            letter-spacing: 0.5px;
            background: #FFEBE5;
            padding: 0.15rem 0.5rem;
            border-radius: 4px;
            margin-bottom: 0.4rem;
        }
        .cheat-title {
            font-family: var(--font-heading);
            font-size: 1rem;
            font-weight: 700;
            color: var(--text-heading);
            margin-bottom: 0.6rem;
        }
        .cheat-formula {
            background: #FFFDF9;
            border: 1px solid var(--border-soft);
            border-radius: 6px;
            padding: 0.6rem;
            margin: 0.5rem 0;
            overflow-x: auto;
        }
        .cheat-solved {
            font-size: 0.85rem;
            color: #4E342E;
            background: #FFF8E1;
            padding: 0.6rem 0.8rem;
            border-radius: 6px;
            margin-top: 0.6rem;
            line-height: 1.5;
            border: 1px dashed #FFE082;
        }

        /* Interactive Quiz Widget */
        .quiz-section {
            background: linear-gradient(135deg, #FFF3E0, #FFE0B2);
            border-radius: var(--radius-lg);
            padding: 2.2rem;
            margin: 3rem 0;
            border: 1px solid var(--border-medium);
        }
        .quiz-header {
            margin-bottom: 1.5rem;
        }
        .quiz-question {
            background: #FFFFFF;
            padding: 1.4rem;
            border-radius: var(--radius-md);
            margin-bottom: 1.2rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.03);
            border: 1px solid var(--border-soft);
        }
        .quiz-q-text {
            font-weight: 600;
            margin-bottom: 0.8rem;
            color: var(--text-heading);
        }
        .quiz-options {
            display: flex;
            flex-direction: column;
            gap: 0.5rem;
        }
        .quiz-opt {
            padding: 0.6rem 1rem;
            background: var(--surface-alt);
            border: 1px solid var(--border-soft);
            border-radius: 6px;
            cursor: pointer;
            font-size: 0.92rem;
            transition: all 0.2s ease;
        }
        .quiz-opt:hover {
            background: #FFE6DB;
            border-color: var(--accent-peach);
        }
        .quiz-opt.correct {
            background: #E8F5E9 !important;
            border-color: #4CAF50 !important;
            color: #2E7D32 !important;
            font-weight: 600;
        }
        .quiz-opt.incorrect {
            background: #FFEBEE !important;
            border-color: #E53935 !important;
            color: #C62828 !important;
        }
        .quiz-explanation {
            margin-top: 0.6rem;
            font-size: 0.88rem;
            padding: 0.6rem;
            border-radius: 4px;
            background: #FFF8E1;
            display: none;
        }

        /* Back to top button */
        #back-to-top {
            position: fixed;
            bottom: 2rem;
            right: 2rem;
            width: 46px;
            height: 46px;
            border-radius: 50%;
            background: var(--primary-dark);
            color: #FFFFFF;
            border: none;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(216, 67, 21, 0.3);
            display: none;
            align-items: center;
            justify-content: center;
            font-size: 1.2rem;
            z-index: 900;
            transition: all 0.2s ease;
        }
        #back-to-top:hover {
            transform: translateY(-3px);
            background: #BF360C;
        }

        /* Footer */
        footer.site-footer {
            background: #2D2424;
            color: #FFE0D6;
            padding: 3rem 1.5rem;
            text-align: center;
            font-size: 0.9rem;
            margin-top: 4rem;
        }
        footer.site-footer a {
            color: var(--accent-peach);
            text-decoration: none;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .hero-title {
                font-size: 1.7rem;
            }
            .search-box input {
                width: 140px;
            }
            .search-box input:focus {
                width: 180px;
            }
            section.module-section {
                padding: 1.8rem 1.2rem;
            }
            header.sticky-header {
                padding: 0 1rem;
            }
            #cheat-sheet-drawer {
                width: 100vw;
            }
        }

        /* ==========================================================================
           DARK THEME (default) — token overrides + hard-coded light surfaces
           ========================================================================== */
        :root[data-theme="dark"] {
            color-scheme: dark;
            --bg-body: #14100E;
            --surface-card: #1E1815;
            --surface-alt: #261E1A;
            --accent-peach-light: #4A2E24;
            --accent-peach: #FFAB91;
            --accent-peach-vivid: #FF8A65;
            --accent-terracotta: #FF7043;
            --primary-dark: #E65A2B;
            --text-heading: #FFE0D6;
            --text-body: #D7CCC8;
            --text-muted: #A1887F;
            --border-soft: #3A2B25;
            --border-medium: #5A3F33;
            --callout-bg: #2A1F18;
            --shadow-card: 0 4px 16px rgba(0,0,0,0.4), 0 2px 6px rgba(0,0,0,0.3);
            --shadow-hover: 0 8px 24px rgba(0,0,0,0.55), 0 3px 8px rgba(0,0,0,0.3);
        }
        [data-theme="dark"] header.sticky-header { background: rgba(20,16,14,0.95); box-shadow: 0 2px 10px rgba(0,0,0,0.4); }
        [data-theme="dark"] #progress-container { background: rgba(255,171,145,0.12); }
        [data-theme="dark"] .hero-banner { background: linear-gradient(135deg, #2A1A14 0%, #3A2118 50%, #4A2A1E 100%); border-color: rgba(255,171,145,0.18); }
        [data-theme="dark"] .hero-banner::before { background: radial-gradient(circle, rgba(255,138,101,0.15) 0%, transparent 70%); }
        [data-theme="dark"] .hero-subtitle { color: #E0CFC8; }
        [data-theme="dark"] .hero-meta { color: #C9B5AC; }
        [data-theme="dark"] .meta-pill { background: rgba(255,255,255,0.06); border-color: rgba(255,171,145,0.25); }
        [data-theme="dark"] .callout-body { color: #D7CCC8; }
        [data-theme="dark"] .callout-note { background-color: #2A1F18; }
        [data-theme="dark"] .callout-warning { background-color: #2C2512; }
        [data-theme="dark"] .callout-important { background-color: #2E1C16; }
        [data-theme="dark"] .callout-caution { background-color: #2E1A1C; }
        [data-theme="dark"] table.custom-table td { border-bottom-color: #3A2B25; }
        [data-theme="dark"] table.custom-table tr:hover td { background-color: #261E1A; }
        [data-theme="dark"] code { background: #3A2620; color: #FFCCBC; }
        [data-theme="dark"] .code-container code { background: transparent; }
        [data-theme="dark"] .problem-card { background: #1E1815; }
        [data-theme="dark"] .problem-statement { background: rgba(255,112,67,0.07); }
        [data-theme="dark"] .solution-details, [data-theme="dark"] .solution-content { background: #1E1815; }
        [data-theme="dark"] .solution-toggle:hover { background: #3A2620; }
        [data-theme="dark"] #cheat-sheet-drawer { background: #14100E; box-shadow: -6px 0 30px rgba(0,0,0,0.6); }
        [data-theme="dark"] .cheat-header { background: linear-gradient(135deg, #3A2118, #4A2A1E); }
        [data-theme="dark"] .cheat-close-btn:hover { background: rgba(255,255,255,0.12); }
        [data-theme="dark"] .cheat-tab-btn, [data-theme="dark"] .cheat-card { background: #1E1815; }
        [data-theme="dark"] .cheat-cat-badge { background: #3A2620; }
        [data-theme="dark"] .cheat-formula { background: #14100E; }
        [data-theme="dark"] .cheat-solved { color: #E0CFC8; background: #2C2512; border-color: #6B5A1F; }
        [data-theme="dark"] .quiz-section { background: linear-gradient(135deg, #261A14, #33201A); }
        [data-theme="dark"] .quiz-section p { color: #C9B5AC !important; }
        [data-theme="dark"] .quiz-question { background: #1E1815; }
        [data-theme="dark"] .quiz-opt:hover { background: #3A2620; }
        [data-theme="dark"] .quiz-opt.correct { background: #14301A !important; border-color: #4CAF50 !important; color: #A5D6A7 !important; }
        [data-theme="dark"] .quiz-opt.incorrect { background: #3A1618 !important; border-color: #E53935 !important; color: #EF9A9A !important; }
        [data-theme="dark"] .quiz-explanation { background: #2C2512; }
        [data-theme="dark"] .search-box input { background: #1E1815; color: var(--text-heading); }
        [data-theme="dark"] .drawer-backdrop { background: rgba(0,0,0,0.65); }
        [data-theme="dark"] footer.site-footer { background: #0D0A09; }

        /* ==========================================================================
           TEST MODE (MCQ quiz overlay)
           ========================================================================== */
        #test-overlay { position: fixed; inset: 0; z-index: 2000; background: var(--bg-body); display: none; overflow-y: auto; }
        #test-overlay.open { display: block; }
        .test-wrap { max-width: 820px; margin: 0 auto; padding: 1.5rem 1.25rem 4rem; }
        .test-topbar { display: flex; justify-content: space-between; align-items: center; gap: 1rem; margin-bottom: 1.25rem; }
        .test-topbar h2 { font-family: var(--font-heading); color: var(--text-heading); font-size: 1.5rem; }
        .test-card { background: var(--surface-card); border: 1px solid var(--border-soft); border-radius: var(--radius-lg); padding: 1.5rem; box-shadow: var(--shadow-card); margin-bottom: 1.25rem; }
        .test-card h3 { font-family: var(--font-heading); color: var(--text-heading); margin-bottom: 0.75rem; font-size: 1.1rem; }
        .test-row { display: flex; flex-wrap: wrap; gap: 0.6rem; align-items: center; }
        .test-chip { display: inline-flex; align-items: center; gap: 0.45rem; padding: 0.45rem 0.9rem; border: 1px solid var(--border-medium); border-radius: 30px; cursor: pointer; font-size: 0.88rem; background: var(--surface-alt); color: var(--text-body); user-select: none; }
        .test-chip.on { background: var(--accent-terracotta); border-color: var(--accent-terracotta); color: #fff; }
        .test-chip input { accent-color: var(--primary-dark); }
        .test-mods { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 0.5rem; margin-top: 0.75rem; }
        .test-mods.disabled { opacity: 0.45; pointer-events: none; }
        .test-mods .test-chip { border-radius: var(--radius-md); font-size: 0.82rem; }
        .test-btn { background: var(--accent-terracotta); color: #fff; border: none; border-radius: 30px; padding: 0.65rem 1.5rem; font-weight: 700; font-size: 0.95rem; cursor: pointer; font-family: inherit; }
        .test-btn:hover { background: var(--primary-dark); }
        .test-btn.ghost { background: transparent; color: var(--text-body); border: 1px solid var(--border-medium); }
        .test-btn.ghost:hover { background: var(--surface-alt); }
        .test-btn:disabled { opacity: 0.4; cursor: not-allowed; }
        .test-select { background: var(--surface-alt); color: var(--text-body); border: 1px solid var(--border-medium); border-radius: 8px; padding: 0.4rem 0.6rem; font-family: inherit; }
        .test-progress { height: 6px; background: var(--border-soft); border-radius: 6px; overflow: hidden; margin-bottom: 1rem; }
        .test-progress > div { height: 100%; background: linear-gradient(90deg, var(--accent-peach), var(--accent-terracotta)); transition: width .25s; }
        .test-meta { display: flex; justify-content: space-between; color: var(--text-muted); font-size: 0.85rem; margin-bottom: 0.6rem; flex-wrap: wrap; gap: .5rem; }
        .test-tag { background: var(--accent-peach-light); color: var(--text-heading); border-radius: 20px; padding: 0.1rem 0.7rem; font-size: 0.75rem; font-weight: 600; }
        .test-q { color: var(--text-heading); font-size: 1.05rem; line-height: 1.65; margin-bottom: 1rem; }
        .test-opt { display: flex; gap: 0.7rem; padding: 0.75rem 1rem; border: 1px solid var(--border-medium); border-radius: var(--radius-md); margin-bottom: 0.55rem; cursor: pointer; background: var(--surface-alt); color: var(--text-body); }
        .test-opt:hover { border-color: var(--accent-terracotta); }
        .test-opt .k { font-weight: 700; color: var(--accent-terracotta); min-width: 1.2rem; }
        .test-opt.locked { pointer-events: none; }
        .test-opt.correct { background: #E8F5E9; border-color: #4CAF50; color: #2E7D32; }
        .test-opt.wrong { background: #FFEBEE; border-color: #E53935; color: #C62828; }
        [data-theme="dark"] .test-opt.correct { background: #14301A; color: #A5D6A7; }
        [data-theme="dark"] .test-opt.wrong { background: #3A1618; color: #EF9A9A; }
        .test-exp { display: none; margin-top: 0.9rem; padding: 0.85rem 1rem; border-left: 4px solid var(--accent-terracotta); background: var(--callout-bg); border-radius: 8px; font-size: 0.92rem; }
        .test-score { font-family: var(--font-heading); font-size: 3rem; color: var(--accent-terracotta); font-weight: 800; }
        .test-bar { display: grid; grid-template-columns: 1fr 70px; gap: .6rem; align-items: center; font-size: .85rem; margin: .35rem 0; }
        .test-bar .track { height: 8px; background: var(--border-soft); border-radius: 6px; overflow: hidden; }
        .test-bar .fill { height: 100%; background: var(--accent-terracotta); }
        .test-review-item { border-top: 1px solid var(--border-soft); padding: 0.9rem 0; font-size: 0.92rem; }
        #theme-toggle-btn { min-width: 2.4rem; justify-content: center; }
        /* ---------- Mobile / narrow screens ---------- */
        @media (max-width: 1100px) {
            #open-cheat-sheet-btn .lbl, #open-eli5-btn .lbl, #open-theory-btn .lbl, #open-test-btn .lbl { display: none; }
        }
        @media (max-width: 900px) {
            :root { --header-height: 108px; }
            header.sticky-header { flex-wrap: wrap; align-content: center; row-gap: 0.45rem; padding: 0.4rem 0.9rem; }
            header.sticky-header > div:first-child { flex: 1 1 100%; justify-content: space-between; }
            .header-brand { font-size: 1rem; gap: 0.5rem; }
            .header-actions { flex: 1 1 100%; gap: 0.4rem; }
            .header-actions .nav-btn { padding: 0.45rem 0.6rem; }
            .search-box { flex: 1 1 auto; min-width: 0; }
            .search-box input, .search-box input:focus { width: 100%; min-width: 0; }
            #toggle-drawer-btn .lbl { display: none; }
            .math-inline { white-space: normal; }
            .hero-banner { padding: 2rem 1.1rem; }
            .meta-pill { white-space: normal; }
            #nav-drawer { width: min(320px, 88vw); }
            h2.module-title { font-size: 1.45rem; line-height: 1.3; }
        }
        @media (max-width: 380px) {
            .brand-badge { display: none; }
        }
    </style>
    <link rel="stylesheet" href="mobile.css">
</head>
<body>

    <!-- Scroll Progress Indicator -->
    <div id="progress-container"><div id="progress-bar"></div></div>

    <!-- Sticky Navigation Bar -->
    <header class="sticky-header">
        <div style="display: flex; align-items: center; gap: 1rem;">
            <button id="toggle-drawer-btn" class="nav-btn" title="Toggle Navigation Drawer">
                <span style="font-size: 1.1rem;">☰</span> <span class="lbl">Modules</span>
            </button>
            <a href="#" class="header-brand">
                <span>Reliability &amp; Stats</span>
                <span class="brand-badge">NPTEL IIT KGP</span>
            </a>
        </div>

        <div class="header-actions">
            <div class="search-box">
                <svg viewBox="0 0 24 24"><path d="M15.5 14h-.79l-.28-.27A6.471 6.471 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19l-4.99-5zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14z"/></svg>
                <input type="text" id="live-search" placeholder="Search formulas, theorems, problem types...">
            </div>
            <a href="theory.html" id="open-theory-btn" class="nav-btn tab-dup" style="text-decoration:none;" title="Necessary theory, definitions and exam traps for every module">
                <span>📖 <span class="lbl">Theory</span></span>
            </a>
            <a href="eli5.html" id="open-eli5-btn" class="nav-btn tab-dup" style="text-decoration:none;" title="Simple, explain-like-I'm-five walkthrough of every module">
                <span>🧸 <span class="lbl">ELI5</span></span>
            </a>
            <button id="open-test-btn" class="nav-btn tab-dup" title="Take an MCQ test on all or selected modules">
                <span>📝 <span class="lbl">Test</span></span>
            </button>
            <button id="theme-toggle-btn" class="nav-btn" title="Toggle light / dark mode" aria-label="Toggle theme"><span>☀️</span></button>
            <button id="open-cheat-sheet-btn" class="nav-btn tab-dup" title="Open Master Formula Reference & Problem Types">
                <span>⚡ <span class="lbl">Cheat Sheet &amp; Formulas</span></span>
            </button>
        </div>
    </header>

    <!-- Sidebar Navigation Drawer -->
    <aside id="nav-drawer">
        <div class="drawer-title">
            <span>COURSE MODULES</span>
            <button id="close-drawer-btn" style="background:none; border:none; font-size:1.2rem; cursor:pointer;">✕</button>
        </div>
        <nav class="drawer-nav">
            <!--NAV_LINKS_PLACEHOLDER-->
        </nav>
    </aside>

    <!-- Hero Banner -->
    <div class="hero-banner">
        <span class="hero-tag">Complete 60-Lecture Master Guide &amp; Handbook</span>
        <h1 class="hero-title">Statistical Learning for Reliability Analysis</h1>
        <p class="hero-subtitle">Comprehensive, mathematically rigorous lecture notes, formulas, and problem archetypes covering probability, inference, ANOVA, regression, and Support Vector Machines.</p>
        <div class="hero-meta">
            <span class="meta-pill">🏛️ Prof. Monalisa Sarma (IIT Kharagpur)</span>
            <span class="meta-pill">📚 12 Modules &amp; 60 Full Lectures</span>
            <span class="meta-pill">🔢 Complete Problem Solving Archetypes</span>
            <span class="meta-pill">💡 Interactive Solutions &amp; Quizzes</span>
        </div>
    </div>

    <!-- Main Study Guide Content -->
    <main class="main-container">
        <!--ALL_MODULES_PLACEHOLDER-->

        <!-- Interactive Self-Assessment Quiz Section -->
        <section class="quiz-section" id="self-assessment-quiz">
            <div class="quiz-header">
                <span class="hero-tag">Interactive Knowledge Check</span>
                <h2 style="font-family: var(--font-heading); color: var(--text-heading); font-size: 1.6rem; margin-top: 0.5rem;">Concept Mastery &amp; Self-Assessment Quizzes</h2>
                <p style="color: #5D4037; font-size: 0.95rem;">Test your theoretical and numerical intuition on key reliability engineering and statistical learning concepts.</p>
            </div>

            <!-- Quiz 1: Bathtub Curve -->
            <div class="quiz-question" data-correct="1">
                <div class="quiz-q-text">1. During Phase II (Useful Life) of the Bathtub Curve, what is the mathematical nature of the hazard rate $h(t)$, and which probability distribution governs time-to-failure?</div>
                <div class="quiz-options">
                    <div class="quiz-opt" data-opt="0">Decreasing hazard rate ($DFR$), governed by Lognormal distribution.</div>
                    <div class="quiz-opt" data-opt="1">Constant hazard rate ($CFR$, $h(t) = \lambda$), governed by Exponential distribution.</div>
                    <div class="quiz-opt" data-opt="2">Linearly increasing hazard rate ($IFR$), governed by Rayleigh distribution.</div>
                    <div class="quiz-opt" data-opt="3">Bell-shaped hazard rate, governed by Normal distribution.</div>
                </div>
                <div class="quiz-explanation">
                    <strong>Explanation:</strong> In Phase II, failures occur predominantly due to random chance overstress shocks at a constant rate $\lambda = \text{const}$, which is uniquely characterized by the memoryless Exponential distribution $R(t) = e^{-\lambda t}$.
                </div>
            </div>

            <!-- Quiz 2: ANOVA F-test -->
            <div class="quiz-question" data-correct="2">
                <div class="quiz-q-text">2. Why is Analysis of Variance (ANOVA) used instead of multiple pairwise two-sample $t$-tests when comparing $k \ge 3$ treatment group means?</div>
                <div class="quiz-options">
                    <div class="quiz-opt" data-opt="0">ANOVA requires fewer assumptions than the two-sample $t$-test.</div>
                    <div class="quiz-opt" data-opt="1">Pairwise $t$-tests inflate the probability of committing a Type II error ($\beta$).</div>
                    <div class="quiz-opt" data-opt="2">Multiple pairwise $t$-tests severely inflate the Family-Wise Type I Error Rate ($\alpha_{\text{FW}} = 1 - (1-\alpha)^m$).</div>
                    <div class="quiz-opt" data-opt="3">ANOVA eliminates the need for calculating within-group sample variances.</div>
                </div>
                <div class="quiz-explanation">
                    <strong>Explanation:</strong> For $k$ groups, there are $m = \binom{k}{2}$ pairwise tests. If each test is conducted at $\alpha = 0.05$, the overall false positive rate inflates to $1 - (0.95)^m$ (e.g., $40.1\%$ for $k=5$). ANOVA evaluates all groups simultaneously in an omnibus $F$-test.
                </div>
            </div>

            <!-- Quiz 3: SVM Support Vectors -->
            <div class="quiz-question" data-correct="0">
                <div class="quiz-q-text">3. In a Hard-Margin Support Vector Machine (SVM), which training data points have strictly positive Lagrange multipliers ($\alpha_i > 0$)?</div>
                <div class="quiz-options">
                    <div class="quiz-opt" data-opt="0">Only the Support Vectors that lie directly on the canonical margin boundaries ($y_i(\mathbf{w}^T \mathbf{x}_i + b) = 1$).</div>
                    <div class="quiz-opt" data-opt="1">All data points in the training set.</div>
                    <div class="quiz-opt" data-opt="2">Points that lie furthest from the separating hyperplane.</div>
                    <div class="quiz-opt" data-opt="3">Only points with misclassification errors.</div>
                </div>
                <div class="quiz-explanation">
                    <strong>Explanation:</strong> By the KKT complementary slackness condition $\alpha_i [y_i(\mathbf{w}^T \mathbf{x}_i + b) - 1] = 0$, any point strictly outside the margin has $y_i(\mathbf{w}^T\mathbf{x}_i+b) > 1 \implies \alpha_i = 0$. Only points with $\alpha_i > 0$ (the Support Vectors on the margin) determine $\mathbf{w}$ and $b$.
                </div>
            </div>

            <!-- Quiz 4: Logistic Regression Odds Ratio -->
            <div class="quiz-question" data-correct="3">
                <div class="quiz-q-text">4. In a logistic regression model $\text{logit}(p) = \beta_0 + \beta_1 X$, what does the exponentiated coefficient $e^{\beta_1}$ represent?</div>
                <div class="quiz-options">
                    <div class="quiz-opt" data-opt="0">The change in the predicted probability $p$ per unit increase in $X$.</div>
                    <div class="quiz-opt" data-opt="1">The Pearson correlation coefficient between $X$ and $Y$.</div>
                    <div class="quiz-opt" data-opt="2">The additive change in the log-odds of success per unit increase in $X$.</div>
                    <div class="quiz-opt" data-opt="3">The multiplicative change in the odds of success per unit increase in $X$ (the Odds Ratio).</div>
                </div>
                <div class="quiz-explanation">
                    <strong>Explanation:</strong> $\beta_1$ represents the additive change in log-odds. Exponentiating yields $\text{Odds}(X+1)/\text{Odds}(X) = e^{\beta_1}$, which is the multiplicative factor by which the odds of failure/success change per unit increase in $X$.
                </div>
            </div>
        </section>
    </main>

    <!-- Master Formula Cheat Sheet & Problem-Solving Drawer -->
    <div id="drawer-backdrop" class="drawer-backdrop"></div>
    <aside id="cheat-sheet-drawer">
        <div class="cheat-header">
            <div class="cheat-header-title">
                <span>⚡ Master Formula Cheat Sheet</span>
            </div>
            <button id="close-cheat-sheet-btn" class="cheat-close-btn">✕</button>
        </div>
        <div class="cheat-filter-bar">
            <button class="cheat-tab-btn active" data-filter="all">All (13)</button>
            <button class="cheat-tab-btn" data-filter="rel">Reliability</button>
            <button class="cheat-tab-btn" data-filter="sys">Systems</button>
            <button class="cheat-tab-btn" data-filter="disc">Discrete</button>
            <button class="cheat-tab-btn" data-filter="cont">Continuous</button>
            <button class="cheat-tab-btn" data-filter="samp">Sampling</button>
            <button class="cheat-tab-btn" data-filter="est">Inference</button>
            <button class="cheat-tab-btn" data-filter="anova">ANOVA</button>
            <button class="cheat-tab-btn" data-filter="reg">Regression</button>
            <button class="cheat-tab-btn" data-filter="svm">SVM</button>
            <input type="text" id="cheat-search" class="cheat-search-input" placeholder="Quick search formula or problem type...">
        </div>
        <div class="cheat-body" id="cheat-body-content">
            <!--CHEAT_CARDS_PLACEHOLDER-->
        </div>
    </aside>

    <!-- Bottom tab bar (phones only, see mobile.css) -->
    <nav class="tabbar" aria-label="Pages">
        <a href="#" aria-current="page"><span class="ic">📘</span>Guide</a>
        <a href="theory.html"><span class="ic">📖</span>Theory</a>
        <a href="eli5.html"><span class="ic">🧸</span>ELI5</a>
        <button type="button" id="tab-formulas"><span class="ic">⚡</span>Formulas</button>
        <button type="button" id="tab-test"><span class="ic">📝</span>Test</button>
    </nav>

    <!-- Back to Top Floating Button -->
    <button id="back-to-top" title="Back to top">↑</button>

    <!-- Footer -->
    <footer class="site-footer">
        <p><strong>Statistical Learning for Reliability Analysis</strong> — Complete Course Study Guide</p>
        <p style="margin-top: 0.5rem; opacity: 0.8;">Based on NPTEL Course Materials by Prof. Monalisa Sarma, Subir Chowdhury School of Quality and Reliability, IIT Kharagpur.</p>
        <p style="margin-top: 0.5rem; font-size: 0.8rem; opacity: 0.6;">Crafted with Bright Peach Aesthetic &amp; MathJax 3 LaTeX Engine.</p>
    </footer>

    <!-- Interactive Scripts -->
    <script>
        // Trigger MathJax Typesetting helper
        function retypesetMath(element) {
            if (window.MathJax && window.MathJax.typesetPromise) {
                if (element) {
                    MathJax.typesetPromise([element]).catch(err => console.log('Typeset error:', err));
                } else {
                    MathJax.typesetPromise().catch(err => console.log('Typeset error:', err));
                }
            }
        }

        // Scroll Progress bar
        window.addEventListener('scroll', () => {
            const winScroll = document.documentElement.scrollTop || document.body.scrollTop;
            const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
            const scrolled = (winScroll / height) * 100;
            document.getElementById('progress-bar').style.width = scrolled + '%';

            // Back to top button visibility
            const btt = document.getElementById('back-to-top');
            if (winScroll > 400) {
                btt.style.display = 'flex';
            } else {
                btt.style.display = 'none';
            }

            // Active scrollspy for sidebar drawer links
            const sections = document.querySelectorAll('section.module-section');
            const navLinks = document.querySelectorAll('.drawer-nav a');
            let currentId = '';
            sections.forEach(sec => {
                const top = sec.offsetTop - 120;
                if (winScroll >= top) {
                    currentId = sec.getAttribute('id');
                }
            });
            navLinks.forEach(link => {
                link.classList.remove('active');
                if (link.getAttribute('href') === '#' + currentId) {
                    link.classList.add('active');
                }
            });
        });

        // Back to top click
        document.getElementById('back-to-top').addEventListener('click', () => {
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        // Navigation Drawer toggle
        const drawer = document.getElementById('nav-drawer');
        document.getElementById('toggle-drawer-btn').addEventListener('click', () => {
            drawer.classList.toggle('open');
        });
        document.getElementById('close-drawer-btn').addEventListener('click', () => {
            drawer.classList.remove('open');
        });
        document.querySelectorAll('.drawer-nav a').forEach(a => {
            a.addEventListener('click', () => {
                drawer.classList.remove('open');
            });
        });

        // Master Formula Cheat Sheet Drawer toggle
        const cheatDrawer = document.getElementById('cheat-sheet-drawer');
        const backdrop = document.getElementById('drawer-backdrop');
        const openCheatBtn = document.getElementById('open-cheat-sheet-btn');
        const closeCheatBtn = document.getElementById('close-cheat-sheet-btn');

        function openCheatSheet() {
            cheatDrawer.classList.add('open');
            backdrop.classList.add('show');
            // Trigger MathJax on open to guarantee crisp formulas
            retypesetMath(cheatDrawer);
        }

        function closeCheatSheet() {
            cheatDrawer.classList.remove('open');
            backdrop.classList.remove('show');
        }

        openCheatBtn.addEventListener('click', openCheatSheet);
        closeCheatBtn.addEventListener('click', closeCheatSheet);
        backdrop.addEventListener('click', closeCheatSheet);
        document.getElementById('tab-formulas').addEventListener('click', openCheatSheet);
        if (location.hash === '#formulas') {
            history.replaceState(null, '', location.pathname + location.search);
            openCheatSheet();
        }

        // Cheat Sheet Category Filtering & Search
        const tabBtns = document.querySelectorAll('.cheat-tab-btn');
        const cheatCards = document.querySelectorAll('.cheat-card');
        const cheatSearch = document.getElementById('cheat-search');

        function filterCheatCards() {
            const activeTab = document.querySelector('.cheat-tab-btn.active').getAttribute('data-filter');
            const searchVal = cheatSearch.value.toLowerCase().trim();

            cheatCards.forEach(card => {
                const cardCat = card.getAttribute('data-cat');
                const cardText = card.innerText.toLowerCase();
                const matchesTab = (activeTab === 'all' || cardCat === activeTab);
                const matchesSearch = (!searchVal || cardText.includes(searchVal));

                if (matchesTab && matchesSearch) {
                    card.style.display = 'block';
                } else {
                    card.style.display = 'none';
                }
            });
            retypesetMath(cheatDrawer);
        }

        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                tabBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');
                filterCheatCards();
            });
        });

        cheatSearch.addEventListener('input', filterCheatCards);

        // Live Search / Filter across Main Course Modules
        const searchInput = document.getElementById('live-search');
        searchInput.addEventListener('input', (e) => {
            const term = e.target.value.toLowerCase().trim();
            const sections = document.querySelectorAll('section.module-section');
            sections.forEach(sec => {
                if (!term) {
                    sec.style.display = 'block';
                    return;
                }
                const text = sec.innerText.toLowerCase();
                if (text.includes(term)) {
                    sec.style.display = 'block';
                } else {
                    sec.style.display = 'none';
                }
            });
        });

        // Trigger MathJax when expanding details accordions
        document.querySelectorAll('details.solution-details').forEach(det => {
            det.addEventListener('toggle', () => {
                if (det.open) {
                    retypesetMath(det);
                }
            });
        });

        // Interactive Quiz Logic
        document.querySelectorAll('.quiz-question').forEach(q => {
            const correctIdx = parseInt(q.getAttribute('data-correct'));
            const options = q.querySelectorAll('.quiz-opt');
            const explanation = q.querySelector('.quiz-explanation');

            options.forEach((opt, idx) => {
                opt.addEventListener('click', () => {
                    options.forEach(o => o.style.pointerEvents = 'none');
                    if (idx === correctIdx) {
                        opt.classList.add('correct');
                        opt.innerHTML += ' ✅ <em>Correct!</em>';
                    } else {
                        opt.classList.add('incorrect');
                        opt.innerHTML += ' ❌ <em>Incorrect</em>';
                        options[correctIdx].classList.add('correct');
                    }
                    if (explanation) {
                        explanation.style.display = 'block';
                        retypesetMath(explanation);
                    }
                });
            });
        });
    </script>

    <!-- MCQ Test Overlay -->
    <div id="test-overlay" role="dialog" aria-modal="true" aria-label="MCQ Test">
        <div class="test-wrap" id="test-root"></div>
    </div>
    <script src="quiz_bank.js"></script>
    <script src="quiz.js"></script>
    <script src="mathfit.js"></script>
</body>
</html>
''')

    with open("template_v2.html", "r", encoding="utf-8") as tf:
        template_str = tf.read()

    final_html = template_str.replace("<!--NAV_LINKS_PLACEHOLDER-->", nav_links_html)
    final_html = final_html.replace("<!--ALL_MODULES_PLACEHOLDER-->", all_modules_html)
    final_html = final_html.replace("<!--CHEAT_CARDS_PLACEHOLDER-->", cheat_sheet_cards)

    with open("index.html", "w", encoding="utf-8") as f_out:
        f_out.write(final_html)
    print(f"index.html successfully created ({len(final_html)} characters).")

    if os.path.exists("template_v2.html"):
        os.remove("template_v2.html")


if __name__ == "__main__":
    build_study_guide()
    build_interactive_html()
    print("Compilation v2.0 complete!")
