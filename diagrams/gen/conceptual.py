"""Conceptual tier diagrams — mental models, metaphors, and systems thinking.

Each diagram maps COSMOS ideas to an intuitive conceptual frame:
  Basic    — one mind, three faculties · the improvement flywheel
  Advanced — recursive generations · the cognition loop (past/present/future)
  Expert   — variation & selection · the meta-ladder (loops about loops)
"""
from design import *


# ── Basic 06: The COSMOS Mind ─────────────────────────────────────────
def cosmos_mind():
    w, h = 1200, 860
    s = [svg_start(w, h, "THE COSMOS MIND",
        "One cognitive system — three faculties mapped to cognitive time")]
    s.append(label(600, 96, "RSIS3 (reason) · MyKB (memory) · SPACE (imagination) — the whole is one mind", 11, TEXT3, italic=True))

    # Central mind
    s.append(box(400, 110, 400, 118, RSIS, "🧠 THE COSMOS MIND", "RSIS3 + MyKB + SPACE — one cognition",
                 title_size=16, header_h=44, rx=16))
    s.append(label(618, 270, "meta-cognition: it watches itself think", 9.5, TEXT4, anchor="start", italic=True))

    # Faculty cards
    cards = [
        (80, MYKB, "🧠", "Memory", "what was learned", "PAST", [
            "2,360+ wiki pages · TF-IDF search",
            "knowledge graph · temporal snapshots",
            "grounds every decision in experience",
            "feeds the present with context",
        ]),
        (435, RSIS, "🔥", "Reason & Action", "what to do now", "PRESENT", [
            "L1 acts · L2 improves · L3 evolves",
            "immutable evaluator gates all changes",
            "executes the system's decisions",
            "the executive that chooses & acts",
        ]),
        (790, SPACE, "✧", "Imagination", "what could be", "FUTURE", [
            "326 probes · 7 series · 25 rounds",
            "RRP → structured specifications",
            "explores options before commitment",
            "challenges memory with new ideas",
        ]),
    ]
    for x, accent, icon, name, role, tense, facts in cards:
        s.append(f'<rect x="{x}" y="300" width="330" height="250" rx="12" fill="{PANEL}" stroke="{accent}" stroke-width="1.4" filter="url(#shadow)"/>')
        s.append(f'<rect x="{x+12}" y="312" width="306" height="26" rx="6" fill="{accent}" opacity=".16"/>')
        s.append(f'<text x="{x+165}" y="330" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="10" font-weight="700" letter-spacing="2">{esc(tense)}</text>')
        s.append(f'<circle cx="{x+42}" cy="378" r="17" fill="{accent}" opacity=".28"/>')
        s.append(f'<text x="{x+42}" y="384" text-anchor="middle" fill="{TEXT}" font-size="15">{icon}</text>')
        s.append(f'<text x="{x+72}" y="376" fill="{accent}" font-family="{FONT}" font-size="17" font-weight="700">{esc(name)}</text>')
        s.append(f'<text x="{x+72}" y="394" fill="{TEXT2}" font-family="{FONT}" font-size="10.5" font-style="italic">{esc(role)}</text>')
        s.append(f'<line x1="{x+14}" y1="410" x2="{x+316}" y2="410" stroke="{BORDER2}" stroke-width="1"/>')
        fy = 430
        for f in facts[:3]:
            s.append(f'<text x="{x+16}" y="{fy}" fill="{TEXT3}" font-family="{FONT}" font-size="10.5">{esc(f)}</text>')
            fy += 20
        s.append(f'<text x="{x+16}" y="{fy+6}" fill="{accent}" opacity=".8" font-family="{FONT}" font-size="9.5" font-style="italic">{esc(facts[3])}</text>')

    # Mind → faculties
    s.append(arrow(600, 228, 215, 300, MYKB, "arwM", 2.5, curve=(480, 250, 320, 280)))
    s.append(arrow(600, 228, 600, 300, RSIS, "arwR", 2.5))
    s.append(arrow(600, 228, 985, 300, SPACE, "arwS", 2.5, curve=(720, 250, 880, 280)))
    # Faculties → mind (feedback)
    s.append(arrow(215, 300, 600, 228, GRAY, "arwG", 1.8, dashed=True, curve=(320, 280, 480, 250)))
    s.append(arrow(600, 300, 600, 228, GRAY, "arwG", 1.8, dashed=True))
    s.append(arrow(985, 300, 600, 228, GRAY, "arwG", 1.8, dashed=True, curve=(880, 280, 720, 250)))

    # Emergence panel
    s.append(panel(80, 600, 1040, 190, DASH, "EMERGENT METACOGNITION", [
        (TEXT2, 11, "Memory grounds reasoning — no decision starts from a blank mind"),
        (TEXT2, 11, "Reasoning tests imagination — speculative ideas must pass the evaluator"),
        (TEXT2, 11, "Imagination challenges memory — new probes question old assumptions"),
        (TEXT4, 10, "Each faculty is weak alone; together they form a self-improving mind"),
    ], header_h=34, line_h=26))
    chips = [("grounded", MYKB), ("tested", RSIS), ("challenged", SPACE), ("compounding", DASH)]
    cx = 140
    for text, color in chips:
        s.append(chip(cx, 742, text, color, size=10.5))
        cx += 108
    s.append(svg_end(w))
    return "\n".join(s)


# ── Basic 07: The Improvement Flywheel ─────────────────────────────────
def improvement_flywheel():
    w, h = 1200, 860
    s = [svg_start(w, h, "THE IMPROVEMENT FLYWHEEL",
        "One full lap makes the next lap easier — gains compound like momentum")]
    s.append(label(600, 96, "ideate → execute → evaluate → consolidate → strategize → (smarter, again)", 10.5, TEXT3, italic=True))

    # Hub
    s.append(f'<circle cx="600" cy="400" r="112" fill="none" stroke="{BORDER2}" stroke-width="1.2" stroke-dasharray="6,5" opacity=".5"/>')
    s.append(f'<circle cx="600" cy="400" r="95" fill="{PANEL}" stroke="{RSIS}" stroke-width="2" filter="url(#shadow)"/>')
    s.append(label(600, 392, "COSMOS", 20, TEXT, font=FONT))
    s.append(label(600, 412, "self-improvement", 10, TEXT2))
    s.append(label(600, 428, "flywheel", 10, TEXT2))
    s.append(label(600, 450, "↻ momentum builds", 9.5, EXT, italic=True))

    # Five stages (clockwise pentagon)
    stages = [
        (600, 170, SPACE, "IDEATE", ["326 probes → spec"], "arwS"),
        (819, 329, RSIS, "EXECUTE", ["run L1 → L2 → L3"], "arwR"),
        (735, 586, EXT, "EVALUATE", ["PASS/FAIL gate"], "arwH"),
        (465, 586, MYKB, "CONSOLIDATE", ["store lessons"], "arwM"),
        (381, 329, DASH, "STRATEGIZE", ["smarter next lap"], "arwD"),
    ]
    for cx, cy, accent, title, line, _m in stages:
        bx, by = cx - 90, cy - 33
        s.append(f'<rect x="{bx}" y="{by}" width="180" height="66" rx="10" fill="{PANEL}" stroke="{accent}" stroke-width="1.5" filter="url(#shadow)"/>')
        s.append(f'<rect x="{bx}" y="{by}" width="180" height="28" rx="10" fill="{accent}" opacity=".16"/>')
        s.append(f'<text x="{cx}" y="{by+19}" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="11" font-weight="700" letter-spacing="1">{esc(title)}</text>')
        s.append(f'<text x="{cx}" y="{by+50}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="9.5">{esc(line[0])}</text>')

    # Clockwise edges (source-color arrows)
    edges = [
        (600, 203, 729, 329, SPACE, "arwS", "specs in"),
        (819, 362, 735, 553, RSIS, "arwR", "candidates"),
        (645, 586, 555, 586, EXT, "arwH", "winners"),
        (465, 553, 381, 362, MYKB, "arwM", "lessons"),
        (381, 296, 510, 170, DASH, "arwD", "smarter prompts"),
    ]
    for x1, y1, x2, y2, color, m, lab in edges:
        s.append(arrow(x1, y1, x2, y2, color, m, 2.5))
        s.append(label((x1 + x2) / 2, (y1 + y2) / 2 - 9, lab, 9, TEXT4, italic=True))

    # Compounding panel
    s.append(f'<rect x="80" y="662" width="1040" height="168" rx="12" fill="{PANEL}" stroke="{BORDER2}" filter="url(#shadow)"/>')
    s.append(label(120, 690, "COMPOUNDING RETURNS — each lap adds momentum", 13, DASH, anchor="start"))
    bars = [(170, 40), (330, 70), (490, 105)]
    for i, (bx, bh) in enumerate(bars):
        s.append(f'<rect x="{bx}" y="{800-bh}" width="70" height="{bh}" rx="6" fill="{DASH}" opacity=".75"/>')
        s.append(f'<text x="{bx+35}" y="818" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="9.5">lap {i+1}</text>')
    s.append(label(700, 734, "Knowledge accumulates · strategies deepen · loops speed up", 11, TEXT2, anchor="start"))
    s.append(label(700, 758, "improvement becomes easier with every lap", 10.5, TEXT3, anchor="start", italic=True))
    s.append(label(1065, 745, "↗", 26, EXT, anchor="middle"))
    s.append(svg_end(w))
    return "\n".join(s)


# ── Advanced 06: Recursive Generations ─────────────────────────────────
def recursive_generations():
    w, h = 1400, 960
    s = [svg_start(w, h, "RECURSIVE GENERATIONS",
        "Standing on your own shoulders — each generation's output is the next generation's input")]
    s.append(label(700, 96, "G0 → G1 → G2 → G3: every generation inherits the last one's work", 10.5, TEXT3, italic=True))

    # Left recursion-depth rail
    s.append(f'<line x1="130" y1="180" x2="130" y2="700" stroke="{GRAY}" stroke-width="2" opacity=".7" marker-end="url(#arwG)"/>')
    s.append(f'<text x="115" y="440" transform="rotate(-90 115 440)" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="10" letter-spacing="1.5">RECURSION DEPTH</text>')

    # Generation rows
    rows = [
        (140, RSIS, "G0", "depth 0 · act", "fresh prompts · empty memory",
         "first specs, session logs, telemetry", "baseline knowledge graph", "🔄 RSIS3 · L1"),
        (300, MYKB, "G1", "depth 1 · improve the actor", "G0's specs + knowledge graph",
         "evaluated improvements, curated memory", "the immutable evaluator gate", "🧠 MyKB · L2"),
        (460, SPACE, "G2", "depth 2 · improve improvement", "G1's strategies + telemetry",
         "refined prompts, tuned loop parameters", "self-tuning L2 improvement", "✧ SPACE · L3"),
        (620, EXT, "G3", "depth 3 · evolve evolution", "G2's refined system",
         "meta-strategies, autonomous L3 evolution", "recursive control of evolution", "🔭 Observer"),
    ]
    for y, accent, gen, depth, inherits, produces, gains, comp in rows:
        s.append(f'<rect x="280" y="{y}" width="1040" height="120" rx="12" fill="{PANEL}" stroke="{BORDER2}" stroke-width="1" filter="url(#shadow)"/>')
        s.append(f'<rect x="280" y="{y}" width="8" height="120" rx="4" fill="{accent}" opacity=".85"/>')
        # badge
        s.append(f'<rect x="310" y="{y+22}" width="130" height="76" rx="8" fill="{accent}" opacity=".15" stroke="{accent}" stroke-width="1" stroke-opacity=".45"/>')
        s.append(f'<text x="375" y="{y+52}" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="24" font-weight="700">{gen}</text>')
        s.append(f'<text x="375" y="{y+74}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="9.5">{esc(depth)}</text>')
        # flows
        s.append(f'<text x="480" y="{y+40}" fill="{TEXT4}" font-family="{FONT}" font-size="10">inherits</text>')
        s.append(f'<text x="565" y="{y+40}" fill="{TEXT2}" font-family="{FONT}" font-size="10.5">{esc(inherits)}</text>')
        s.append(f'<text x="480" y="{y+66}" fill="{TEXT4}" font-family="{FONT}" font-size="10">produces</text>')
        s.append(f'<text x="565" y="{y+66}" fill="{TEXT2}" font-family="{FONT}" font-size="10.5">{esc(produces)}</text>')
        s.append(f'<text x="480" y="{y+92}" fill="{accent}" font-family="{FONT}" font-size="10.5" font-weight="700">gains</text>')
        s.append(f'<text x="565" y="{y+92}" fill="{accent}" opacity=".9" font-family="{FONT}" font-size="10.5">{esc(gains)}</text>')
        # component chip
        s.append(chip(1130, y + 42, comp, accent, size=10.5))
        # arrow between rows
        if y > 140:
            s.append(arrow(900, y - 40, 900, y, GRAY, "arwG", 2.2, opacity=0.7))

    # Loopback (right rail)
    s.append(f'<path d="M 1335 700 C 1370 600, 1370 300, 1335 220" fill="none" stroke="{EXT}" stroke-width="2" stroke-dasharray="7,5" opacity=".8" marker-end="url(#arwH)"/>')
    s.append(f'<text x="1355" y="460" transform="rotate(90 1355 460)" text-anchor="middle" fill="{EXT}" font-family="{FONT}" font-size="9.5" font-style="italic">consolidated memory + evolved strategy loop back</text>')

    # Principle panel
    s.append(panel(80, 780, 1240, 100, DASH, "THE RECURSION PRINCIPLE", [
        (TEXT2, 10.5, "Each generation stands on the previous one's shoulders — its outputs become the next generation's inputs."),
        (TEXT2, 10.5, "Improvement compounds: knowledge, strategy, and prompts are inherited, so every cycle reasons from a stronger base."),
    ], header_h=30, line_h=24, pad=16))
    s.append(svg_end(w))
    return "\n".join(s)


# ── Advanced 07: The Cognition Loop ────────────────────────────────────
def cognition_loop():
    w, h = 1400, 960
    s = [svg_start(w, h, "THE COGNITION LOOP",
        "Past · Present · Future — one decision integrates memory, reasoning, and imagination")]
    s.append(label(700, 96, "every action is a point where what-was and what-could-be meet", 10.5, TEXT3, italic=True))

    # Three tense cards
    cards = [
        (90, MYKB, "🧠", "Memory", "what was learned", "PAST", [
            "2,360+ wiki pages · TF-IDF search",
            "knowledge graph · temporal snapshots",
        ]),
        (505, RSIS, "🔥", "Reason & Action", "what to do now", "PRESENT", [
            "L1 acts · L2 improves · L3 evolves",
            "immutable evaluator gates changes",
        ]),
        (920, SPACE, "✧", "Imagination", "what could be", "FUTURE", [
            "326 probes · 7 series · RRP specs",
            "7 LLM providers project scenarios",
        ]),
    ]
    for x, accent, icon, name, role, tense, facts in cards:
        s.append(f'<rect x="{x}" y="140" width="390" height="170" rx="12" fill="{PANEL}" stroke="{accent}" stroke-width="1.4" filter="url(#shadow)"/>')
        s.append(f'<rect x="{x+12}" y="152" width="366" height="26" rx="6" fill="{accent}" opacity=".16"/>')
        s.append(f'<text x="{x+195}" y="170" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="10" font-weight="700" letter-spacing="2">{esc(tense)}</text>')
        s.append(f'<circle cx="{x+42}" cy="220" r="16" fill="{accent}" opacity=".28"/>')
        s.append(f'<text x="{x+42}" y="226" text-anchor="middle" fill="{TEXT}" font-size="14">{icon}</text>')
        s.append(f'<text x="{x+70}" y="218" fill="{accent}" font-family="{FONT}" font-size="16" font-weight="700">{esc(name)}</text>')
        s.append(f'<text x="{x+70}" y="236" fill="{TEXT2}" font-family="{FONT}" font-size="10.5" font-style="italic">{esc(role)}</text>')
        fy = 262
        for f in facts:
            s.append(f'<text x="{x+16}" y="{fy}" fill="{TEXT3}" font-family="{FONT}" font-size="10.5">{esc(f)}</text>')
            fy += 20

    # Lateral flows (two arrows per gap)
    s.append(arrow(480, 200, 505, 200, MYKB, "arwM", 2.2))
    s.append(arrow(505, 235, 480, 235, RSIS, "arwR", 2.2, opacity=0.75))
    s.append(label(492, 192, "context", 8.5, TEXT4, italic=True))
    s.append(label(493, 248, "results", 8.5, TEXT4, italic=True))
    s.append(arrow(920, 200, 895, 200, SPACE, "arwS", 2.2))
    s.append(arrow(895, 235, 920, 235, RSIS, "arwR", 2.2, opacity=0.75))
    s.append(label(908, 192, "scenarios", 8.5, TEXT4, italic=True))
    s.append(label(907, 248, "outcomes", 8.5, TEXT4, italic=True))

    # Down into NOW
    s.append(arrow(285, 310, 620, 420, MYKB, "arwM", 2.4, curve=(380, 340, 480, 360)))
    s.append(label(430, 342, "context", 9.5, TEXT4, italic=True))
    s.append(arrow(700, 310, 700, 420, RSIS, "arwR", 2.4))
    s.append(label(712, 372, "decide", 9.5, TEXT4, anchor="start", italic=True))
    s.append(arrow(1115, 310, 780, 420, SPACE, "arwS", 2.4, curve=(1020, 340, 920, 360)))
    s.append(label(985, 342, "scenarios", 9.5, TEXT4, italic=True))

    # NOW node
    s.append(box(520, 420, 360, 110, DASH, "⚡ NOW — DECIDE & ACT", "integrate memory + scenarios → act", title_size=14, header_h=38))
    s.append(label(700, 486, "L1 acts · L2 improves · L3 evolves", 10, TEXT3))
    s.append(label(700, 508, "one action — grounded in past, aimed at future", 9.5, TEXT3, italic=True))

    # Feedback loops
    s.append(arrow(700, 530, 285, 620, MYKB, "arwM", 2.4, curve=(560, 590, 420, 600)))
    s.append(label(430, 570, "results stored → memory", 9.5, MYKB, anchor="start"))
    s.append(arrow(700, 530, 1115, 620, SPACE, "arwS", 2.4, curve=(840, 590, 980, 600)))
    s.append(label(1000, 570, "outcomes recalibrate forecasts", 9.5, SPACE, anchor="end"))
    s.append(panel(90, 620, 390, 88, MYKB, "MEMORY UPDATED", [
        (TEXT3, 10, "lessons → knowledge graph & snapshots"),
    ], header_h=28, line_h=18, pad=12))
    s.append(panel(920, 620, 390, 88, SPACE, "FORECASTS RECALIBRATED", [
        (TEXT3, 10, "outcomes refine future scenarios"),
    ], header_h=28, line_h=18, pad=12))

    # Why time matters
    s.append(panel(80, 740, 1240, 130, DASH, "WHY TIME MATTERS", [
        (TEXT2, 10.5, "Grounding — every decision starts from remembered experience (MyKB supplies context)"),
        (TEXT2, 10.5, "Foresight — every decision is tested against imagined futures (SPACE supplies scenarios)"),
        (TEXT2, 10.5, "Action — the present is where past and future meet; RSIS3 executes with both in hand"),
    ], header_h=32, line_h=24, pad=16))
    s.append(svg_end(w))
    return "\n".join(s)


# ── Expert 05: Variation & Selection ───────────────────────────────────
def variation_selection():
    w, h = 1600, 1060
    s = [svg_start(w, h, "VARIATION & SELECTION",
        "The evolutionary engine — generate many, test hard, keep winners, inherit them")]
    s.append(label(800, 96, "good ideas are not designed — they are generated, tested, and kept", 10.5, TEXT3, italic=True))

    # 2x2 cards
    s.append(box(150, 190, 560, 220, SPACE, "VARIATION", "generate many — SPACE", icon="①", title_size=15, header_h=44))
    for i, f in enumerate(["326 probes · 7 series · 25 rounds", "diverse candidate specifications", "7 LLM providers → built-in variety", "variety beats cleverness"]):
        s.append(label(200, 288 + i * 26, f, 10.5, TEXT3 if i < 3 else SPACE, anchor="start"))
    s.append(box(890, 190, 560, 220, EXT, "SELECTION", "test hard — the evaluator", icon="②", title_size=15, header_h=44))
    for i, f in enumerate(["SHA-256 integrity check", "isolated subprocess execution", "PASS/FAIL gate — no mercy", "trust nothing unproven"]):
        s.append(label(940, 288 + i * 26, f, 10.5, TEXT3 if i < 3 else EXT, anchor="start"))
    s.append(box(890, 520, 560, 220, RSIS, "INHERITANCE", "pass it on — RSIS3", icon="③", title_size=15, header_h=44))
    for i, f in enumerate(["winners become the new baseline", "L3 evolves strategy across sessions", "every generation starts stronger", "a compounding baseline"]):
        s.append(label(940, 618 + i * 26, f, 10.5, TEXT3 if i < 3 else RSIS, anchor="start"))
    s.append(box(150, 520, 560, 220, MYKB, "RETENTION", "keep winners — MyKB", icon="④", title_size=15, header_h=44))
    for i, f in enumerate(["winners → knowledge graph entries", "session artifacts + wiki pages", "temporal snapshots preserve history", "memory is the gene pool"]):
        s.append(label(200, 618 + i * 26, f, 10.5, TEXT3 if i < 3 else MYKB, anchor="start"))

    # Cycle arrows
    s.append(arrow(710, 300, 890, 300, GRAY, "arwG", 2.5))
    s.append(label(800, 292, "candidates", 9.5, TEXT4, italic=True))
    s.append(arrow(1170, 410, 1170, 520, GRAY, "arwG", 2.5))
    s.append(label(1182, 470, "winners", 9.5, TEXT4, anchor="start", italic=True))
    s.append(arrow(890, 630, 710, 630, GRAY, "arwG", 2.5))
    s.append(label(800, 622, "outcomes", 9.5, TEXT4, italic=True))
    s.append(arrow(430, 520, 430, 410, GRAY, "arwG", 2.5))
    s.append(label(418, 470, "context", 9.5, TEXT4, anchor="end", italic=True))

    # Center
    s.append(f'<rect x="700" y="445" width="200" height="70" rx="10" fill="{PANEL}" stroke="{DASH}" stroke-width="1.4" stroke-dasharray="5,4"/>')
    s.append(label(800, 472, "survival of the", 10.5, DASH, font=FONT))
    s.append(label(800, 492, "fittest ideas", 10.5, DASH, font=FONT))

    # BVSR panel
    s.append(panel(100, 800, 1400, 115, EXT, "BLIND VARIATION · SELECTIVE RETENTION", [
        (TEXT2, 10.5, "No idea is trusted in advance — SPACE generates many candidates because the system cannot know which will work."),
        (TEXT2, 10.5, "The immutable evaluator is the selection pressure: integrity checks, isolated runs, PASS/FAIL. Only winners persist."),
        (TEXT2, 10.5, "MyKB is the gene pool — what survives becomes the inheritance every future generation starts from."),
    ], header_h=32, line_h=25, pad=16))
    s.append(svg_end(w))
    return "\n".join(s)


# ── Expert 06: The Meta-Ladder ─────────────────────────────────────────
def meta_ladder():
    w, h = 1600, 1060
    s = [svg_start(w, h, "THE META-LADDER",
        "Loops about loops — each level reasons about the level below it")]
    s.append(label(800, 96, "recursive self-improvement is a ladder: L1 acts · L2 improves the actor · L3 evolves evolution · the observer watches", 10.5, TEXT3, italic=True))

    # Rails
    s.append(f'<line x1="210" y1="200" x2="210" y2="780" stroke="{GRAY}" stroke-width="2" opacity=".7" marker-end="url(#arwG)"/>')
    s.append(f'<text x="195" y="490" transform="rotate(-90 195 490)" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="10" letter-spacing="1.5">DEEPER ABSTRACTION</text>')
    s.append(f'<line x1="1390" y1="200" x2="1390" y2="780" stroke="{GRAY}" stroke-width="2" opacity=".7" marker-end="url(#arwG)"/>')
    s.append(f'<text x="1405" y="490" transform="rotate(-90 1405 490)" text-anchor="middle" fill="{TEXT4}" font-family="{FONT}" font-size="10" letter-spacing="1.5">LONGER TIMESCALE</text>')

    # Rungs
    rungs = [
        (190, RSIS, "L0", "action loop", "ACTION LOOP (L1) — operates on tasks in the world",
         "tool calls · observations · retries", "closes the loop in seconds", "⏱ seconds", "out: task + raw log"),
        (350, MYKB, "L1", "improvement loop", "IMPROVEMENT LOOP (L2) — operates on the actor (L1)",
         "code generation · prompt tuning", "rewrites the agent that acts", "⏱ minutes", "out: better agent + prompts"),
        (510, SPACE, "L2", "evolution loop", "EVOLUTION LOOP (L3) — operates on improvement itself",
         "memory consolidation · strategy evolution", "selects which improvements survive", "⏱ hours–days", "out: evolved strategy"),
        (670, EXT, "L3", "the observer", "THE OBSERVER — SPACE probes + immutable evaluator",
         "326 probes audit hidden assumptions", "SHA-256 + PASS/FAIL gate on all changes", "⏱ continuous", "out: trust, not blind faith"),
    ]
    for y, accent, lvl, sub, title, f1, f2, tchip, ochip in rungs:
        s.append(f'<rect x="250" y="{y}" width="1100" height="120" rx="12" fill="{PANEL}" stroke="{BORDER2}" stroke-width="1" filter="url(#shadow)"/>')
        s.append(f'<rect x="250" y="{y}" width="8" height="120" rx="4" fill="{accent}" opacity=".85"/>')
        s.append(f'<rect x="280" y="{y+22}" width="120" height="76" rx="8" fill="{accent}" opacity=".15" stroke="{accent}" stroke-width="1" stroke-opacity=".45"/>')
        s.append(f'<text x="340" y="{y+52}" text-anchor="middle" fill="{accent}" font-family="{FONT}" font-size="24" font-weight="700">{lvl}</text>')
        s.append(f'<text x="340" y="{y+76}" text-anchor="middle" fill="{TEXT3}" font-family="{FONT}" font-size="9.5">{esc(sub)}</text>')
        s.append(f'<text x="450" y="{y+40}" fill="{TEXT2}" font-family="{FONT}" font-size="12" font-weight="700">{esc(title)}</text>')
        s.append(f'<text x="450" y="{y+68}" fill="{TEXT3}" font-family="{FONT}" font-size="10.5">{esc(f1)}</text>')
        s.append(f'<text x="450" y="{y+92}" fill="{TEXT3}" font-family="{FONT}" font-size="10.5">{esc(f2)}</text>')
        s.append(chip(1130, y + 30, tchip, accent, size=10))
        s.append(chip(1130, y + 62, ochip, accent, size=10))
        if y > 190:
            s.append(arrow(800, y - 40, 800, y, GRAY, "arwG", 2.2, opacity=0.7))

    # Loopback
    s.append(f'<path d="M 1460 750 C 1490 600, 1490 400, 1460 250" fill="none" stroke="{EXT}" stroke-width="2" stroke-dasharray="7,5" opacity=".8" marker-end="url(#arwH)"/>')
    s.append(f'<text x="1475" y="500" transform="rotate(90 1475 500)" text-anchor="middle" fill="{EXT}" font-family="{FONT}" font-size="9.5" font-style="italic">observer findings feed the next action cycle</text>')

    # Ladder principle
    s.append(panel(100, 830, 1400, 90, DASH, "CLIMBING THE LADDER", [
        (TEXT2, 10.5, "Recursive self-improvement is a ladder: L1 executes, L2 improves the executor, L3 evolves the improvement strategy."),
        (TEXT2, 10.5, "The observer sits outside the loops so nothing is changed blindly — every rung refactors the one below."),
    ], header_h=30, line_h=24, pad=16))
    s.append(svg_end(w))
    return "\n".join(s)


CONCEPTUAL = {
    "basic-06-cosmos-mind.svg": cosmos_mind,
    "basic-07-improvement-flywheel.svg": improvement_flywheel,
    "advanced-06-recursive-generations.svg": recursive_generations,
    "advanced-07-cognition-loop.svg": cognition_loop,
    "expert-05-variation-selection.svg": variation_selection,
    "expert-06-meta-ladder.svg": meta_ladder,
}
