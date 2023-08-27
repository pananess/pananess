_printContent: function() {
    var kbc = $(this.container).find('.kbViewContainer');

    var iframe = document.createElement('iframe');
    $(this.container).append(iframe);

    iframe.contentWindow.document.open();

    // styling can be modified
    iframe.contentWindow.document.write(`
        <style>
            img { max-width: 100%; }
            .attachment-link {
                display: inline-flex;
                align-items: center;
                padding: 5px;
                border: 1px solid #ccc;
                border-radius: 4px;
                text-decoration: none;
                margin: 5px 0;
            }
            .attachment-icon {
                width: 16px;
                height: 16px;
                margin-right: 5px;
            }
        </style>\n` + this.renderedValue);

    iframe.contentWindow.document.close();

    // rendering to add icons to attachment links (editable)
    var attachmentLinks = iframe.contentWindow.document.querySelectorAll('a[href$=".pdf"], a[href$=".doc"], a[href$=".docx"]');
    for (var i = 0; i < attachmentLinks.length; i++) {
        var link = attachmentLinks[i];

        var icon = document.createElement('img');
        icon.src = 'path-to-attachment-icon.png'; // update with the real path
        icon.alt = 'Attachment';
        icon.className = 'attachment-icon';
        
        var attachmentLink = document.createElement('div');
        attachmentLink.className = 'attachment-link';
        attachmentLink.appendChild(icon);
        
        while (link.firstChild) {
            attachmentLink.appendChild(link.firstChild);
        }
        
        link.parentNode.replaceChild(attachmentLink, link);
    }

    iframe.addEventListener("load", function(e) {
        iframe.contentWindow.print();
        iframe.remove();
    }.bind(this));
},
