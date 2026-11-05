
import "./App.css";

const modules = [
  {
    code: "01",
    name: "Produtos",
    description: "Cadastro, consulta e gerenciamento de produtos.",
  },
  {
    code: "02",
    name: "Estoque",
    description: "Entradas, saídas e ajustes de mercadorias.",
  },
  {
    code: "03",
    name: "Vendas",
    description: "Registro de vendas e controle de pagamentos.",
  },
  {
    code: "04",
    name: "Caixa",
    description: "Abertura, movimentações e fechamento.",
  },
  {
    code: "05",
    name: "Relatórios",
    description: "Consultas e acompanhamento operacional.",
  },
  {
    code: "06",
    name: "Usuários",
    description: "Contas, perfis e permissões de acesso.",
  },
];

const indicators = [
  "Produtos cadastrados",
  "Vendas realizadas",
  "Caixa atual",
];

function App() {
  return (
    <div className="app-shell">
      <aside className="sidebar">
        <div className="brand">
          <img src="/logo.png" alt="Logo CentralBeer" />
          <div>
            <strong>CentralBeer</strong>
            <span>GESTÃO DE DISTRIBUIDORA</span>
          </div>
        </div>

        <div className="sidebar-label">MENU PRINCIPAL</div>

        <nav className="navigation">
          <div className="nav-item active">
            <span className="nav-code">00</span>
            Visão geral
          </div>

          {modules.map((module) => (
            <div className="nav-item disabled" key={module.code}>
              <span className="nav-code">{module.code}</span>
              {module.name}
            </div>
          ))}
        </nav>

        <div className="sidebar-footer">
          <span className="status-dot" />
          Ambiente de desenvolvimento
        </div>
      </aside>

      <div className="main-area">
        <header className="topbar">
          <div>
            <span className="topbar-label">CENTRALBEER / PAINEL</span>
            <p>Gestão da distribuidora</p>
          </div>

          <span className="environment-tag">
            DESENVOLVIMENTO
          </span>
        </header>

        <main className="content">
          <section className="welcome-section">
            <div>
              <span className="eyebrow">VISÃO GERAL</span>
              <h1>Bem-vindo ao CentralBeer.</h1>
              <p>
                Centralize a gestão de produtos, estoque,
                vendas e caixa em um único lugar.
              </p>
            </div>

            <div className="welcome-symbol">CB</div>
          </section>

          <section className="section-block">
            <div className="section-heading">
              <div>
                <h2>Indicadores</h2>
                <p>
                  Informações operacionais do estabelecimento.
                </p>
              </div>
            </div>

            <div className="indicator-grid">
              {indicators.map((indicator, index) => (
                <article className="indicator-card" key={indicator}>
                  <span className="indicator-number">
                    0{index + 1}
                  </span>
                  <h3>{indicator}</h3>
                  <strong>—</strong>
                  <span className="card-caption">
                    Aguardando integração com o backend
                  </span>
                </article>
              ))}
            </div>
          </section>

          <section className="section-block">
            <div className="section-heading">
              <div>
                <h2>Módulos do sistema</h2>
                <p>
                  Acesse as áreas que compõem o CentralBeer.
                </p>
              </div>
            </div>

            <div className="module-grid">
              {modules.map((module) => (
                <article className="module-card" key={module.code}>
                  <div className="module-card-header">
                    <span className="module-code">
                      {module.code}
                    </span>
                    <span className="planned-tag">
                      PLANEJADO
                    </span>
                  </div>

                  <h3>{module.name}</h3>
                  <p>{module.description}</p>
                </article>
              ))}
            </div>
          </section>

          <footer className="main-footer">
            CentralBeer © 2026 · Gestão de estoque, vendas e caixa.
          </footer>
        </main>
      </div>
    </div>
  );
}

export default App;
