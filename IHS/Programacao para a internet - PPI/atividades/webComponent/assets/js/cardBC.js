export class cardBC extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        let img = this.getAttribute('img');
        let titulo = this.getAttribute('inputtitle');
        let botao = this.getAttribute('inputbtn')
        let conteudo = this.innerHTML;
        this.innerHTML = `
            <div class="card" style="width: 18rem;">
                <img class="card-img-top" src="${img}" alt="Card image cap">
                <div class="card-body">
                    <h5 class="card-title">${titulo}</h5>
                    <p class="card-text">${conteudo}</p>
                    <a href="#" class="btn btn-primary">${botao}</a>
                </div>
            </div>
        `
    }
}
