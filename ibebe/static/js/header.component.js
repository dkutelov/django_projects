class FlexibleHeader extends HTMLElement {
    constructor() {
        super();
        this.attachShadow({ mode: 'open' });
        let logoTemplate = document.getElementById('logo-template');
        this.logoTmp = logoTemplate.content.cloneNode(true);
        this.shadowRoot.appendChild(this.logoTmp);
    }

    connectedCallback() {
        window.addEventListener(
            'scroll',
            this._handleSmallHeaderClass.bind(this)
        );
    }

    _handleSmallHeaderClass(e) {
        if (window.scrollY > 15 ) {
            this.classList.add('header--small')
        } else {
            this.classList.remove('header--small');
        }
    }
}

customElements.define('flexible-header', FlexibleHeader);