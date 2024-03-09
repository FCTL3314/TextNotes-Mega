const $removeNotesBtn = $("#removeNotesBtn");

const NOTE_APPEARING_ANIMATION_CLASS = "animate__animated animate__fadeIn"

function createNoteHTML(id, title, text, created, with_animation=true) {
    return `
        <div
            class="col-6 col-md-4 col-lg-3 col-xl-3 col-xxl-3 ${with_animation ? NOTE_APPEARING_ANIMATION_CLASS : ""}"
            data-note-id="${id}"
        >
            <div class="note-item rounded-5 shadow-sm">
                <div class="note-content component shadow-none">
                    <div class="d-flex mb-1">
                        <a class="note-content__title link-primary" href="#">
                            ${title}
                        </a>
                        <span class="ms-auto text-muted">${created}</span>
                    </div>
                    <div>
                        <p class="note-content__text">
                            ${text}
                        </p>
                    </div>
                </div>
                <button
                        class="btn btn-outline-primary note__select-btn fw-semibold border-0"
                >
                    Select
                </button>
            </div>
        </div>
        `
}

function selectNote() {
    const $noteItem = $(this).closest('.note-item');
    $noteItem.toggleClass("selected-note");

    const $selectNoteBtn = $(this)

    if ($noteItem.hasClass("selected-note")) {
        $selectNoteBtn.text("Unselect");
    } else {
        $selectNoteBtn.text("Select");
    }
}

function createNoteElements(id, title, text, created, with_animation= true) {
    const $note = $(createNoteHTML(id, title, text, created, with_animation));
    if (with_animation) {
        $note.on("animationend", () => $note.removeClass(NOTE_APPEARING_ANIMATION_CLASS));
    }
    const $selectBtn = $note.find(".note__select-btn");

    const $notesWrp = $('#notesWrp');
    $selectBtn.click(selectNote);

    return {$note, $notesWrp};
}

function appendNote(id, title, text, created, with_animation= true) {
    const {$note, $notesWrp} = createNoteElements(id, title, text, created, with_animation);
    $notesWrp.append($note);
}

function prependNote(id, title, text, created, with_animation= true) {
    const {$note, $notesWrp} = createNoteElements(id, title, text, created, with_animation);
    $notesWrp.prepend($note);
}

function removeNotes() {
    const idsToRemove = [];
    const elementsToRemove = [];

    $(".selected-note").each(function () {
        const $noteEl = $(this).parent();

        elementsToRemove.push($noteEl);
        idsToRemove.push($noteEl.data("noteId"))
    });

    $.ajax({
        url: "/notes/api/notes/delete/",
        method: "DELETE",
        headers: {
            "Content-Type": "application/json",
            ...getCSRFHeader(),
        },
        data: JSON.stringify({
            ids: idsToRemove,
        }),
        success: function () {
            elementsToRemove.forEach(function (el) {
                el.addClass("animate__animated animate__bounceOut");
                el.on("animationend", () => el.remove());
            });
        },
        error: function (error) {
            console.log(error);
        },
    });
}

$removeNotesBtn.click(removeNotes);
