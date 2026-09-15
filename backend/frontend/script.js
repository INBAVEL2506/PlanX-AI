const form = document.getElementById("projectForm");
const analyzeBtn = document.getElementById("analyzeBtn");

const aiLoading = document.getElementById("aiLoading");
const results = document.getElementById("results");

form.addEventListener("submit", async function (event) {
    event.preventDefault();

    analyzeBtn.disabled = true;
    analyzeBtn.textContent = "🤖 Analyzing...";

    aiLoading.classList.add("active");
    results.classList.add("hidden");

    const data = {
        student: {
            name: document.getElementById("studentName").value,
            academic_year: document.getElementById("academicYear").value,
            skills: getList("skills"),
            experience_level: document.getElementById("experience").value,
            interests: getList("interests")
        },

        project: {
            project_name: document.getElementById("projectName").value,
            description: document.getElementById("description").value,
            project_type: document.getElementById("projectType").value,
            available_days: Number(
                document.getElementById("availableDays").value
            ),
            technology_preferences: getList("technologies"),
            constraints: getList("constraints")
        }
    };

    try {
        const response = await fetch(
            "http://127.0.0.1:8000/project",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(data)
            }
        );

        if (!response.ok) {
            throw new Error("Backend returned an error.");
        }

        const result = await response.json();

        displayResults(result);

        aiLoading.classList.remove("active");
        results.classList.remove("hidden");

        results.scrollIntoView({
            behavior: "smooth"
        });

    } catch (error) {

        aiLoading.classList.remove("active");

        alert(
            "Unable to connect to PlanX AI backend.\n\n" +
            "Make sure the FastAPI server is running."
        );

        console.error(error);

    } finally {

        analyzeBtn.disabled = false;
        analyzeBtn.textContent = "🤖 Analyze My Project";
    }
});


function getList(id) {

    return document
        .getElementById(id)
        .value
        .split(",")
        .map(item => item.trim())
        .filter(item => item.length > 0);
}


function displayResults(data) {

    displayDashboard(data);

    createTimeline(data);

    createSkillGap(data);

    displayStudent(data.student);

    displayRequirements(data.requirement_analysis);

    displayTechnologies(data.technology_analysis);

    displayProjectPlan(data.project_plan);

    displayLearningPlan(data.learning_plan);

    displayResources(data.resource_recommendations);

    displayExecutionRoadmap(data.execution_roadmap);

    addPlanControls(data);
}


/* Dashboard */

function displayDashboard(data) {

    const difficulty =
        data.requirement_analysis.difficulty;

    const available =
        data.project.available_days;

    const planned =
        data.project_plan.total_planned_days;

    const skillGap =
        data.project_plan.skill_gap || [];

    document.getElementById("difficulty").textContent =
        difficulty;

    document.getElementById("availableResult").textContent =
        available + " days";

    document.getElementById("plannedDays").textContent =
        planned + " days";

    document.getElementById("skillGapCount").textContent =
        skillGap.length;

    console.log("PlanX AI Dashboard Updated");
}


/* Student */

function displayStudent(student) {

    document.getElementById("studentResult").innerHTML = `

        <p>
            <strong>Name:</strong>
            ${escapeHTML(student.name)}
        </p>

        <p>
            <strong>Academic Year:</strong>
            ${escapeHTML(student.academic_year)}
        </p>

        <p>
            <strong>Experience:</strong>
            ${escapeHTML(student.experience_level)}
        </p>

        <h4>Skills</h4>

        <div>
            ${createTags(student.skills)}
        </div>

        <h4>Interests</h4>

        <div>
            ${createTags(student.interests)}
        </div>
    `;
}


/* Requirements */

function displayRequirements(analysis) {

    document.getElementById("requirementResult").innerHTML = `

        <p>
            <strong>Difficulty:</strong>
            ${escapeHTML(analysis.difficulty)}
        </p>

        <h4>Requirements</h4>

        ${createList(analysis.requirements)}

        <h4>Required Skills</h4>

        ${createTags(analysis.required_skills)}

    `;
}


/* Technologies */

function displayTechnologies(data) {

    let html = `

        <h4>Recommended Technologies</h4>

        <div>
            ${createTags(data.recommended_technologies)}
        </div>

        <h4>Why These Technologies?</h4>

        ${createList(data.reasons)}

        <h4>Student Skill Matches</h4>

        ${createTags(data.student_skill_matches)}
    `;

    document.getElementById("technologyResult").innerHTML =
        html;
}


/* Project Plan */

function displayProjectPlan(plan) {

    let html = `

        <p>
            <strong>Total Planned Days:</strong>
            ${plan.total_planned_days}
        </p>

        <p>
            <strong>Difficulty:</strong>
            ${escapeHTML(plan.difficulty)}
        </p>

        <h4>Skill Gap</h4>

        ${createTags(plan.skill_gap || [])}
    `;

    plan.phases.forEach(phase => {

        html += `

            <h4>
                Phase ${phase.phase}: 
                ${escapeHTML(phase.name)}
            </h4>

            <p>
                <strong>Duration:</strong>
                ${phase.duration} days
            </p>

            ${createList(phase.tasks)}
        `;
    });

    document.getElementById("projectPlanResult").innerHTML =
        html;
}


/* Learning Plan */

function displayLearningPlan(plan) {

    let html = `

        <p>
            <strong>Experience Level:</strong>
            ${escapeHTML(plan.experience_level)}
        </p>
    `;

    plan.skills_to_learn.forEach(skill => {

        html += `

            <h4>
                ${escapeHTML(skill.skill)}
            </h4>

            <p>
                <strong>Duration:</strong>
                ${skill.duration} days
            </p>

            <p>
                <strong>Topics:</strong>
            </p>

            ${createList(skill.topics)}
        `;
    });

    html += `

        <p>
            <strong>Total Learning Days:</strong>
            ${plan.total_learning_days}
        </p>
    `;

    document.getElementById("learningResult").innerHTML =
        html;
}


/* Resources */

function displayResources(data) {

    let html = `

        <p>
            <strong>Experience Level:</strong>
            ${escapeHTML(data.experience_level)}
        </p>
    `;

    data.recommendations.forEach(item => {

        html += `

            <h4>
                ${escapeHTML(item.skill)}
            </h4>
        `;

        item.resources.forEach(resource => {

            html += `

                <a
                    class="resource-link"
                    href="${escapeAttribute(resource.url)}"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    📖 ${escapeHTML(resource.title)}
                    <small>
                        (${escapeHTML(resource.type)})
                    </small>
                </a>
            `;
        });

        html += `

            <p>
                <strong>Practice Tasks</strong>
            </p>

            ${createList(item.practice_tasks)}
        `;
    });

    document.getElementById("resourceResult").innerHTML =
        html;
}


/* Execution Roadmap */

function displayExecutionRoadmap(data) {

    let html = "";

    const roadmap =
        data.daily_roadmap || [];

    roadmap.forEach(day => {

        html += `
            <div class="timeline-item">

                <div class="day">
                    DAY ${day.day}
                </div>

                <div class="phase">
                    PHASE ${day.phase} —
                    ${escapeHTML(day.phase_name)}
                </div>

                <div class="task">
                    ${escapeHTML(day.task)}
                </div>

            </div>
        `;
    });

    if (roadmap.length === 0) {

        html = `
            <p>
                No execution roadmap available.
            </p>
        `;
    }

    document.getElementById("executionResult").innerHTML =
        html;
}


/* Create HTML list */

function createList(items) {

    if (!items || items.length === 0) {
        return "<p>No information available.</p>";
    }

    return `
        <ul>
            ${items.map(item => `
                <li>${escapeHTML(item)}</li>
            `).join("")}
        </ul>
    `;
}


/* Create tags */

function createTags(items) {

    if (!items || items.length === 0) {
        return "<span>No information</span>";
    }

    return items.map(item => `
        <span class="tag">
            ${escapeHTML(item)}
        </span>
    `).join("");
}


/* Security helpers */

function escapeHTML(value) {

    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
}


function escapeAttribute(value) {

    return String(value)
        .replace(/&/g, "&amp;")
        .replace(/"/g, "&quot;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
}



function createTimeline(data) {

    const phases = data.project_plan.phases || [];

    let currentDay = 1;
    let html = "";

    phases.forEach(phase => {

        const startDay = currentDay;
        const endDay = currentDay + phase.duration - 1;

        const progress =
            (phase.duration / data.project_plan.total_planned_days) * 100;

        html += `
            <div class="timeline-card">

                <div class="timeline-header">

                    <div>
                        <span class="phase-number">
                            PHASE ${phase.phase}
                        </span>

                        <h3>${escapeHTML(phase.name)}</h3>
                    </div>

                    <span class="duration">
                        ${phase.duration} Days
                    </span>

                </div>

                <div class="timeline-days">
                    Day ${startDay} – Day ${endDay}
                </div>

                <div class="progress-bar">
                    <div
                        class="progress-fill"
                        style="width: ${progress}%">
                    </div>
                </div>

                <ul>
                    ${phase.tasks.map(task => `
                        <li>${escapeHTML(task)}</li>
                    `).join("")}
                </ul>

            </div>
        `;

        currentDay = endDay + 1;
    });

    const timelineContainer =
        document.getElementById("projectTimeline");

    if (timelineContainer) {
        timelineContainer.innerHTML = html;
    }
}

function createSkillGap(data) {

    const skillGap =
        data.project_plan.skill_gap || [];

    const container =
        document.getElementById("skillGapContainer");

    if (!container) {
        return;
    }

    if (skillGap.length === 0) {
        container.innerHTML = `
            <div class="no-skill-gap">
                🎉 No major skill gaps detected!
            </div>
        `;
        return;
    }

    const icons = {
        "Machine Learning": "🤖",
        "OpenCV": "👁️",
        "Data Processing": "📊"
    };

    container.innerHTML = skillGap.map(skill => {

        const icon = icons[skill] || "📚";

        return `
            <div class="skill-card">

                <div class="skill-icon">
                    ${icon}
                </div>

                <div class="skill-info">

                    <h3>${escapeHTML(skill)}</h3>

                    <span class="skill-status">
                        NEED TO LEARN
                    </span>

                </div>

            </div>
        `;

    }).join("");
}


/* =========================================
   PLANX AI - ACTION CONTROLS
========================================= */

function addPlanControls(data) {

    const results = document.getElementById("results");

    if (!results) {
        return;
    }

    const oldControls = document.getElementById("planControls");

    if (oldControls) {
        oldControls.remove();
    }

    const controls = document.createElement("div");

    controls.id = "planControls";

    controls.innerHTML = `
        <div class="plan-controls">

            <button
                class="plan-action download-action"
                id="downloadPlanBtn">
                📥 Download Plan
            </button>

            <button
                class="plan-action pdf-action"
                id="downloadPdfBtn">
                📄 Download PDF
            </button>

            <button
                class="plan-action print-action"
                id="printPlanBtn">
                🖨️ Print Plan
            </button>

            <button
                class="plan-action"
                id="newPlanBtn">
                🔄 Plan Another Project
            </button>

        </div>
    `;

    results.appendChild(controls);


    /* =========================
       DOWNLOAD JSON PLAN
    ========================= */

    const downloadPlanBtn =
        document.getElementById("downloadPlanBtn");

    if (downloadPlanBtn) {

        downloadPlanBtn.addEventListener("click", function () {

            const jsonData =
                JSON.stringify(data, null, 2);

            const blob = new Blob(
                [jsonData],
                { type: "application/json" }
            );

            const url =
                URL.createObjectURL(blob);

            const link =
                document.createElement("a");

            link.href = url;

            link.download =
                "PlanX-AI-" +
                (data.project?.project_name || "Project")
                    .replace(/\s+/g, "-") +
                "-Plan.json";

            document.body.appendChild(link);

            link.click();

            document.body.removeChild(link);

            URL.revokeObjectURL(url);

        });

    }


    /* =========================
       DOWNLOAD PDF
    ========================= */

    const downloadPdfBtn =
        document.getElementById("downloadPdfBtn");

    if (downloadPdfBtn) {

        downloadPdfBtn.addEventListener("click", function () {

            if (!window.jspdf) {

                alert("PDF generator is not available.");

                return;
            }

            const { jsPDF } = window.jspdf;

            const pdf = new jsPDF();

            const projectName =
                data.project?.project_name ||
                "Project";

            let y = 20;

            pdf.setFontSize(20);

            pdf.text(
                "PlanX AI - Project Plan",
                20,
                y
            );

            y += 12;

            pdf.setFontSize(14);

            pdf.text(
                "Project: " + projectName,
                20,
                y
            );

            y += 10;

            pdf.setFontSize(11);

            pdf.text(
                "Student: " +
                (data.student?.name || ""),
                20,
                y
            );

            y += 8;

            pdf.text(
                "Academic Year: " +
                (data.student?.academic_year || ""),
                20,
                y
            );

            y += 8;

            pdf.text(
                "Experience: " +
                (data.student?.experience_level || ""),
                20,
                y
            );

            y += 12;

            pdf.setFontSize(14);

            pdf.text(
                "Project Plan",
                20,
                y
            );

            y += 10;

            pdf.setFontSize(11);

            const plan =
                data.project_plan;

            if (plan) {

                pdf.text(
                    "Difficulty: " +
                    (plan.difficulty || ""),
                    20,
                    y
                );

                y += 8;

                pdf.text(
                    "Total Planned Days: " +
                    (plan.total_planned_days || ""),
                    20,
                    y
                );

                y += 12;

                const phases =
                    plan.phases || [];

                phases.forEach(phase => {

                    if (y > 270) {

                        pdf.addPage();

                        y = 20;
                    }

                    pdf.setFontSize(12);

                    pdf.text(
                        "Phase " +
                        phase.phase +
                        ": " +
                        phase.name,
                        20,
                        y
                    );

                    y += 7;

                    pdf.setFontSize(10);

                    pdf.text(
                        "Duration: " +
                        phase.duration +
                        " days",
                        25,
                        y
                    );

                    y += 7;

                    const tasks =
                        phase.tasks || [];

                    tasks.forEach(task => {

                        if (y > 275) {

                            pdf.addPage();

                            y = 20;
                        }

                        const lines =
                            pdf.splitTextToSize(
                                "• " + task,
                                165
                            );

                        pdf.text(
                            lines,
                            30,
                            y
                        );

                        y +=
                            lines.length * 5 + 2;

                    });

                    y += 5;

                });

            }

            pdf.save(
                "PlanX-AI-" +
                projectName
                    .replace(/\s+/g, "-") +
                "-Plan.pdf"
            );

        });

    }


    /* =========================
       PRINT PLAN
    ========================= */

    const printPlanBtn =
        document.getElementById("printPlanBtn");

    if (printPlanBtn) {

        printPlanBtn.addEventListener(
            "click",
            function () {

                window.print();

            }
        );

    }


    /* =========================
       PLAN ANOTHER PROJECT
    ========================= */

    const newPlanBtn =
        document.getElementById("newPlanBtn");

    if (newPlanBtn) {

        newPlanBtn.addEventListener(
            "click",
            function () {

                form.reset();

                results.classList.add("hidden");

                aiLoading.classList.remove("active");

                window.scrollTo({
                    top: 0,
                    behavior: "smooth"
                });

            }
        );

    }

}
/* =========================================================
   PLANX AI — NEURAL SPACE ENGINE V3
   ========================================================= */

(function initNeuralSpace() {

    const canvas = document.getElementById("neuralCanvas");

    if (!canvas) return;

    const ctx = canvas.getContext("2d");

    let width = 0;
    let height = 0;
    let animationFrame;

    const mouse = {
        x: 0.5,
        y: 0.5,
        targetX: 0.5,
        targetY: 0.5
    };

    const nodes = [];

    const NODE_COUNT =
        window.innerWidth < 700 ? 38 : 75;

    function resizeCanvas() {

        const dpr = Math.min(
            window.devicePixelRatio || 1,
            2
        );

        width = window.innerWidth;
        height = window.innerHeight;

        canvas.width = width * dpr;
        canvas.height = height * dpr;

        canvas.style.width = width + "px";
        canvas.style.height = height + "px";

        ctx.setTransform(
            dpr,
            0,
            0,
            dpr,
            0,
            0
        );
    }

    function createNode() {

        const depth =
            Math.random();

        return {
            x: Math.random() * width,
            y: Math.random() * height,

            vx:
                (Math.random() - 0.5)
                * (0.12 + depth * 0.18),

            vy:
                (Math.random() - 0.5)
                * (0.12 + depth * 0.18),

            depth: depth,

            radius:
                1.2 + depth * 2.5,

            opacity:
                0.18 + depth * 0.65,

            pulse:
                Math.random() * Math.PI * 2,

            pulseSpeed:
                0.008 + Math.random() * 0.018
        };
    }

    function createNodes() {

        nodes.length = 0;

        for (let i = 0; i < NODE_COUNT; i++) {
            nodes.push(createNode());
        }
    }

    function drawGlow(x, y, radius, alpha) {

        const glow =
            ctx.createRadialGradient(
                x,
                y,
                0,
                x,
                y,
                radius * 8
            );

        glow.addColorStop(
            0,
            `rgba(255, 166, 60, ${alpha})`
        );

        glow.addColorStop(
            0.35,
            `rgba(255, 138, 0, ${alpha * 0.35})`
        );

        glow.addColorStop(
            1,
            "rgba(255, 138, 0, 0)"
        );

        ctx.fillStyle = glow;

        ctx.beginPath();

        ctx.arc(
            x,
            y,
            radius * 8,
            0,
            Math.PI * 2
        );

        ctx.fill();
    }

    function drawConnection(a, b, distance) {

        const maxDistance = 175;

        if (distance > maxDistance) return;

        const strength =
            1 - distance / maxDistance;

        const alpha =
            strength
            * 0.20
            * (0.35 + a.depth * 0.65);

        ctx.beginPath();

        ctx.moveTo(a.x, a.y);

        ctx.lineTo(b.x, b.y);

        ctx.strokeStyle =
            `rgba(255, 166, 60, ${alpha})`;

        ctx.lineWidth =
            0.45 + strength * 0.7;

        ctx.stroke();

        /*
         * Small energy pulse moving through
         * selected neural connections.
         */

        if (
            strength > 0.45 &&
            Math.random() < 0.012
        ) {

            const progress =
                Math.random();

            const px =
                a.x +
                (b.x - a.x)
                * progress;

            const py =
                a.y +
                (b.y - a.y)
                * progress;

            drawGlow(
                px,
                py,
                1.4,
                0.65
            );
        }
    }

    function updateNodes() {

        for (const node of nodes) {

            node.x += node.vx;
            node.y += node.vy;

            node.pulse += node.pulseSpeed;

            /*
             * Very subtle mouse parallax.
             */

            const parallaxX =
                (mouse.x - 0.5)
                * node.depth
                * 12;

            const parallaxY =
                (mouse.y - 0.5)
                * node.depth
                * 8;

            node.renderX =
                node.x + parallaxX;

            node.renderY =
                node.y + parallaxY;

            if (node.x < -30)
                node.x = width + 30;

            if (node.x > width + 30)
                node.x = -30;

            if (node.y < -30)
                node.y = height + 30;

            if (node.y > height + 30)
                node.y = -30;
        }
    }

    function drawNodes() {

        for (const node of nodes) {

            const pulse =
                0.75 +
                Math.sin(node.pulse)
                * 0.25;

            const radius =
                node.radius * pulse;

            const alpha =
                node.opacity * pulse;

            drawGlow(
                node.renderX,
                node.renderY,
                radius,
                alpha * 0.35
            );

            ctx.beginPath();

            ctx.arc(
                node.renderX,
                node.renderY,
                radius,
                0,
                Math.PI * 2
            );

            ctx.fillStyle =
                `rgba(255, 190, 80, ${alpha})`;

            ctx.fill();
        }
    }

    function drawConnections() {

        for (let i = 0; i < nodes.length; i++) {

            for (
                let j = i + 1;
                j < nodes.length;
                j++
            ) {

                const a = nodes[i];
                const b = nodes[j];

                const dx =
                    a.renderX - b.renderX;

                const dy =
                    a.renderY - b.renderY;

                const distance =
                    Math.sqrt(
                        dx * dx +
                        dy * dy
                    );

                drawConnection(
                    a,
                    b,
                    distance
                );
            }
        }
    }

    function animate() {

        ctx.clearRect(
            0,
            0,
            width,
            height
        );

        mouse.x +=
            (mouse.targetX - mouse.x)
            * 0.025;

        mouse.y +=
            (mouse.targetY - mouse.y)
            * 0.025;

        updateNodes();

        drawConnections();

        drawNodes();

        animationFrame =
            requestAnimationFrame(animate);
    }

    window.addEventListener(
        "resize",
        () => {

            resizeCanvas();
            createNodes();

        }
    );

    window.addEventListener(
        "mousemove",
        (event) => {

            mouse.targetX =
                event.clientX / width;

            mouse.targetY =
                event.clientY / height;

        },
        { passive: true }
    );

    resizeCanvas();

    createNodes();

    animate();

})();


