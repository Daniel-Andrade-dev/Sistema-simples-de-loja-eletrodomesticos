#Sistema de loja eletrodomesticos
#Sistema simples feito com python, para simular uma loja de eletrodomésticos
from time import sleep

produtos_disponiveis = {
   "geladeira": 2500,
   "notebook": 5000,
   "tv": 3000,
   "computador": 4500,
   "micro-ondas": 1500
}

historico_de_compras = []

def title() -> str:
   return (
      "\n𝘽𝙚𝙢-𝙑𝙞𝙣𝙙𝙤 𝙖 𝙇𝙤𝙟𝙖 𝙙𝙚 𝙀𝙡𝙚𝙩𝙧𝙤𝙙𝙤𝙢é𝙨𝙩𝙞𝙘𝙤𝙨🖥️"
   )
   

def menu():
   return (
      "\n[1] - Ver produtos"
      "\n[2] - Pagar a vista (10% de desconto)"
      "\n[3] - Pagar parcelado em 12x (com juros 15%)"
      "\n[4] - Pagar parcelado em 3x (sem juros)"
      "\n[5] - Ver histórico de compras"
      "\n[6] - Sair"
   )
   
def ver_produtos(produtos_disponiveis, time=1) -> None:
    print("Carregando produtos 🔄")
    sleep(time)
    print("\nProdutos disponíveis 🛒")
    for produto, preco in produtos_disponiveis.items():
        print(f"{produto.capitalize()}: R${preco:.2f}")
       
        
def pagar_a_vista(produtos_disponiveis,produto,time=2):  
    
    if produto not in produtos_disponiveis:
       return "Produto não encontrado❌"
   
    valor_produto = produtos_disponiveis[produto]
    
    desconto = valor_produto * 0.10
    total_a_pagar =  valor_produto - desconto
    
    historico_de_compras.append({
         "produto": produto,
         "preco": total_a_pagar,
         "parcelas": 0,
         "valor_parcela":0,
         "desconto": desconto
        })
        
    print("Processando pagamento Aguarde 💸")
    sleep(time)
    return (
       "Compra Realizada com sucesso ✅"
        f"\nO produto de {valor_produto:.2f}"
        f"\nSairá por {total_a_pagar:.2f} com 10% desconto"
   )
      
def pagar_parcelado_12_vezes(produtos_disponiveis,produto,time=2):
     
    if produto not in produtos_disponiveis:
        return "Produto não encontrado ❌"
    
    valor_produto = produtos_disponiveis[produto]
    
    
    PARCELAS = 12
    TAXA_JUROS = 0.15
    
    juros = valor_produto * TAXA_JUROS
    total_com_juros = valor_produto + juros
    valor_parcelado = total_com_juros / PARCELAS
    
    historico_de_compras.append({
         "produto": produto,
         "preco": valor_produto,
         "parcelas": 12,
         "valor_parcela": valor_parcelado,
         "desconto": 0
        })
        
    print("Processando pagamento Aguarde 💸 ")
    sleep(time)
   
    return (
       "Compra realizada com sucesso ✅"
        f"\nProduto: {produto}"
        f"\nValor do Produto: R$ {valor_produto:.2f}"
        f"\nValor com juros: R$ {total_com_juros:.2f}"
        f"\nParcelado em {PARCELAS}x de R$ {valor_parcelado:.2f}"
    )


   
def pagar_parcelado_3_vezes(produtos_disponiveis,produto,time=2):
   
   if produto not in produtos_disponiveis:
      return "Produto não encontrado ❌"
      
   valor_produto = produtos_disponiveis[produto]
      
   PARCELAS = 3
   valor_parcelado = valor_produto / PARCELAS
   
   historico_de_compras.append({
         "produto": produto,
         "preco": valor_produto,
         "parcelas": 3,
         "valor_parcela": valor_parcelado,
         "desconto": 0
        })
   print("Processando pagamento Aguarde 💸 ")
   sleep(time)
   return (
      "\nCompra realizada com sucesso ✅"
      f"\nProduto: {produto}"
      f"\nPreço: {valor_produto:.2f}"
      f"\nParcelado em {PARCELAS}x de R${valor_parcelado:.2f}"
   )
   
def mostrar_historico(historico_de_compras) -> None:
      if not historico_de_compras:
         print("Nenhuma compra localizada❌")
      else:
         for compra in historico_de_compras:
            print(
            f"\nProduto: {compra['produto']} | "
            f"\nPreço: R${compra['preco']:.2f} | "
            f"\nParcelas: {compra['parcelas']} | "
            f"\nValor das parcela: R${compra['valor_parcela']:.2f}"
            f"\n💸 Desconto para pagamento à vista: R$ {compra['desconto']:.2f}"
            )
 
def main():
    print(title())
    while True:
       print(menu())
       try:
          
          op = int(input("Informe a opção: "))
       
          if op == 1:
            ver_produtos(produtos_disponiveis)
          elif op == 2:
            produto = input("Informe o (produto) que deseja comprar: ")
            print(pagar_a_vista(produtos_disponiveis,produto))
          elif op == 3:
            produto = input("Informe o (produto) que deseja comprar: ")
            print(pagar_parcelado_12_vezes(produtos_disponiveis,produto))
          elif op == 4:
            produto = input("Informe o (produto) que deseja comprar: ")
            print(pagar_parcelado_3_vezes(produtos_disponiveis,produto))
          elif op == 5:
           mostrar_historico(historico_de_compras)
          elif op == 6:
              print("Você saiu do sistema")
              break
          else:
             print("Opção invalida ❌ ")
       except ValueError:
          print("Digite apenas números🔢")
      
    
if __name__ == "__main__":
   main()