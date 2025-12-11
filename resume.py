import tkinter as tk
from tkinter import messagebox, filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from textwrap import wrap
from reportlab.lib.utils import ImageReader

profile_photo_path = None

# --------- Upload Photo ---------
def upload_photo():
    global profile_photo_path
    profile_photo_path = filedialog.askopenfilename(
        filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
    )
    if profile_photo_path:
        messagebox.showinfo("Photo Selected", f"Selected: {profile_photo_path}")

# --------- Generate PDF Resume ---------
def generate_pdf_resume():
    optimize = optimize_var.get()
    name = entry_name.get().strip()
    email = entry_email.get().strip()
    phone = entry_phone.get().strip()
    summary = text_summary.get("1.0", tk.END).strip()
    skills = text_skills.get("1.0", tk.END).strip()
    experience = text_experience.get("1.0", tk.END).strip()
    projects = text_projects.get("1.0", tk.END).strip()
    education = text_education.get("1.0", tk.END).strip()
    links = text_links.get("1.0", tk.END).strip()

    if not name or not email or not phone:
        messagebox.showerror("Missing Info", "Name, Email, and Phone are required.")
        return

    file_name = f"{name.replace(' ', '_')}_Resume.pdf"
    c = canvas.Canvas(file_name, pagesize=A4)

    width, height = A4
    y = height - 60
    margin_bottom = 60

    # --------- Check Page Break ---------
    def check_page_break(line_height=16):
        nonlocal y
        if y < margin_bottom + line_height:
            c.showPage()
            y = height - 60

    # --------- Draw Section ---------
    def draw_section(title, content, wrap_width=95):
        nonlocal y
        if not content.strip():
            return

        if optimize:
            title_font = 12
            text_font = 9
            line_height = 11
            section_spacing = 5
            wrap_width = 110
        else:
            title_font = 13
            text_font = 10
            line_height = 14
            section_spacing = 12

        check_page_break(line_height + 5)

        c.setFont("Helvetica-Bold", title_font)
        c.drawString(50, y, title.upper())
        y -= (title_font + 5)

        # Special handling for projects (bold project name, normal tech stack)
        if title.lower() == "projects":
            for line in content.split("\n"):
                if not line.strip():
                    continue
                # Split by '-' or ':'
                if '-' in line:
                    parts = line.split('-', 1)
                elif ':' in line:
                    parts = line.split(':', 1)
                else:
                    parts = [line.strip(), '']

                project_name = parts[0].strip()
                project_details = parts[1].strip() if len(parts) > 1 else ''

                # Draw project name bold
                wrapped_name = wrap(project_name, wrap_width)
                for w in wrapped_name:
                    check_page_break(line_height)
                    c.setFont("Helvetica-Bold", text_font)
                    c.drawString(60, y, w)
                    y -= line_height

                # Draw project details normal
                if project_details:
                    wrapped_details = wrap(project_details, wrap_width)
                    for w in wrapped_details:
                        check_page_break(line_height)
                        c.setFont("Helvetica", text_font)
                        c.drawString(70, y, w)
                        y -= line_height

                y -= 5  # spacing between projects
        else:
            for line in content.split("\n"):
                wrapped = wrap(line, wrap_width)
                for w in wrapped:
                    check_page_break(line_height)
                    c.setFont("Helvetica", text_font)
                    c.drawString(60, y, w)
                    y -= line_height

        y -= section_spacing

    # --------- HEADER ---------
    if optimize:
        header_name_font = 16
        header_info_font = 9
        photo_width = 80
        photo_height = 80
    else:
        header_name_font = 20
        header_info_font = 11
        photo_width = 120
        photo_height = 120

    c.setFont("Helvetica-Bold", header_name_font)
    c.drawString(50, y, name)

    # Insert profile photo
    if profile_photo_path:
        try:
            img = ImageReader(profile_photo_path)
            c.drawImage(img, width - 160, y - 10, width=photo_width, height=photo_height, mask='auto')
        except:
            pass

    y -= (header_name_font + 10)
    c.setFont("Helvetica", header_info_font)
    c.drawString(50, y, f"Email: {email}")
    y -= (header_info_font + 4)
    c.drawString(50, y, f"Phone: {phone}")
    y -= (header_info_font + 15)

    # Divider line
    c.setLineWidth(0.5)
    c.line(50, y, width - 50, y)
    y -= 20

    # Draw all sections
    draw_section("Professional Summary", summary)
    draw_section("Skills", skills)
    draw_section("Experience", experience)
    draw_section("Projects", projects)
    draw_section("Education", education)
    draw_section("Links", links)

    c.save()
    messagebox.showinfo("Success", f"Resume saved as {file_name}!")

# --------- GUI ---------
root = tk.Tk()
root.title("WHYAIRESUME CRAFT")

fields = [
    ("Full Name", "entry_name"),
    ("Email", "entry_email"),
    ("Phone", "entry_phone"),
    ("Professional Summary", "text_summary"),
    ("Skills", "text_skills"),
    ("Experience", "text_experience"),
    ("Projects (include URLs)", "text_projects"),
    ("Education", "text_education"),
    ("Links (Portfolio/GitHub/LinkedIn)", "text_links")
]

widgets = {}

for i, (label, key) in enumerate(fields):
    tk.Label(root, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
    if key.startswith("entry"):
        widgets[key] = tk.Entry(root, width=60)
        widgets[key].grid(row=i, column=1, pady=5)
    else:
        widgets[key] = tk.Text(root, height=4, width=60, wrap=tk.WORD)
        widgets[key].grid(row=i, column=1, pady=5)

entry_name        = widgets["entry_name"]
entry_email       = widgets["entry_email"]
entry_phone       = widgets["entry_phone"]
text_summary      = widgets["text_summary"]
text_skills       = widgets["text_skills"]
text_experience   = widgets["text_experience"]
text_projects     = widgets["text_projects"]
text_education    = widgets["text_education"]
text_links        = widgets["text_links"]

# Upload Photo Button
tk.Button(root, text="Upload Photo", command=upload_photo).grid(
    row=len(fields), column=0, pady=10
)

# Optimize length checkbox
optimize_var = tk.BooleanVar()
tk.Checkbutton(root, text="Optimize Resume Length (Fit One Page)", variable=optimize_var).grid(
    row=len(fields), column=1, pady=5, sticky="w"
)

# Generate Resume Button
tk.Button(root, text="Generate PDF Resume", command=generate_pdf_resume).grid(
    row=len(fields)+1, column=1, pady=20
)

root.mainloop()
