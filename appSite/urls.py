from django.urls import path
from .views import TelaView, UserView, ProdutoView, CarrinhoView

# from . import views


urlpatterns = [

    path('login/', TelaView.tela_login, name='telaLogin'),
    path('cadastro-usuario/', TelaView.tela_cadastro_usuario, name='telaCadastroUsuario'),
    path('carrinho/', TelaView.tela_carrinho, name='telaCarrinho'),
    path('checkout/', TelaView.tela_checkout, name='telaCheckout'),
    path('cadastro-produto/', TelaView.tela_cadastro_produto, name='telaCadastroProduto'),
    path('redes-sociais/', TelaView.tela_redes, name='telaRedes'),
    path('base/', TelaView.base, name='base'),
    
    path('registro/', UserView.registro, name='registro'),
    path('entrar/', UserView.entrar, name='entrar'),
    path('sair/', UserView.sair, name='sair'),

    path('cadastrar-produto/', ProdutoView.cadastrar_produto, name='cadastrar_produto'),
    path('listar-todos-produtos/', ProdutoView.listar_todos_produtos, name='listar_todos_produtos'),
    path('editar-produto/<int:produto_id>/', ProdutoView.editar_produto, name='editar_produto'),
    path('excluir-produto/<int:produto_id>/', ProdutoView.excluir_produto, name='excluir_produto'),
    path('', ProdutoView.listar_produtos, name='listar_produtos'),
    path('detalhes-produto/<int:produto_id>/', ProdutoView.detalhes_produto, name='detalhes_produto'),

    path('adicionar-carrinho/<int:produto_id>/', CarrinhoView.adicionar_carrinho, name='adicionar_carrinho'),
    path('remover-item-carrinho/<int:produto_id>/', CarrinhoView.remover_item_carrinho, name='remover_item_carrinho'),
    path('pagamento/', CarrinhoView.tela_pagamento, name='tela_pagamento'),
    path('finalizar-pagamento/', CarrinhoView.finalizar_pagamento, name='finalizar_pagamento'),










#     # FUNÇÕES DAS TELAS
#     path('', views.listar_produtos, name='listar_produtos'),
#     path('telaLogin/', views.telaLogin, name = 'telaLogin'),
#     path('telaCadastroUsuario/', views.telaCadastroUsuario, name = 'telaCadastroUsuario'),
#     path('telaCarrinho/', views.telaCarrinho, name = 'telaCarrinho'),
#     path('telaCheckout/', views.telaCheckout, name = 'telaCheckout'),
#     path('telaCadastroProduto/', views.telaCadastroProduto, name = 'telaCadastroProduto'),
#     path('pagamento/', views.tela_pagamento, name='tela_pagamento'),
#     path('base/', views.base, name = 'base'),
#     path('telaRedes/', views.telaRedes, name = 'telaRedes'),
# # ---------------------------------------------------------------------------------------------------------------------
#     # FUNÇÕES DOS PRODUTOS
#     path('listar_todos_produtos/', views.listar_todos_produtos, name='listar_todos_produtos'),
#     path('cadastrar_produto/', views.cadastrar_produto, name = 'cadastrar_produto'),
#     path('editar_produto/<int:produto_id>/', views.editar_produto, name='editarProduto'),
#     path('excluir_produto/<int:produto_id>/', views.excluir_produto, name='excluirProduto'),
# # ---------------------------------------------------------------------------------------------------------------------
#     # FUNÇÕES DO CARRINHO
#     path('adicionar_carrinho/<int:produto_id>/', views.adicionar_carrinho, name='adicionar_carrinho'),
#     path('remover_item_carrinho/<int:produto_id>/', views.remover_item_carrinho, name='remover_item_carrinho'),
#     path('finalizar_pagamento/', views.finalizar_Pagamento, name='finalizar_pagamento'),
#     path('detalhes_produto/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
# # ---------------------------------------------------------------------------------------------------------------------
#     # FUNÇÕES DO USUÁRIO
#     path('resistro/', views.registro, name = 'registro'),
#     path('entrar/', views.entrar, name = 'entrar'),
#     path('sair/', views.sair, name = 'sair'),
]
