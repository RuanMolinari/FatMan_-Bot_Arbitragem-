# FatMan - Arbitragem Real em DEXs (BSC)

Um bot de arbitragem descentralizada executando trades reais entre DEXs como PancakeSwap, ApeSwap e SushiSwap na BNB Chain.

## 🚀 Recursos
- Execução de trades reais com limite de 10 USDT por arbitragem
- Monitoramento de múltiplos tokens (XRP, ADA, BNB, SOL)
- Verificação de oportunidades entre DEXs
- Proteção contra MEV e frontrunning
- Logging detalhado

## 🛠 Instalação

```bash
git clone https://github.com/seu_usuario/FatMan.git
cd FatMan
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt

⚙️ Configuração
Crie o arquivo .env com base no .env.example:

ini
Copiar
Editar
PRIVATE_KEY=SuaChavePrivada
WALLET=SeuEnderecoWallet
RPC_URL=https://bsc-dataseed.binance.org/
▶️ Execução
bash
Copiar
Editar
python fatman_executor.py
📄 Licença
MIT

yaml
Copiar
Editar

---

### ✅ 2. `.env.example`

```env
PRIVATE_KEY=CHAVE_PRIVADA_AQUI
WALLET=0xSEU_ENDERECO
RPC_URL=https://bsc-dataseed.binance.org/
✅ 3. requirements.txt
txt
Copiar
Editar
web3
python-dotenv
