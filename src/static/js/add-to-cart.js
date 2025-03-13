const cart = {};

  document.querySelectorAll('.add-to-cart').forEach(button => {
    button.addEventListener('click', function () {
      const productId = this.getAttribute('data-product-id');
      cart[productId] = (cart[productId] || 0) + 1;

      console.log(`Product ${productId} added to cart. Current cart:`, cart);
    
    });
  });

  function proceedToCheckout() {
    const form = document.createElement('form');
    form.method = 'POST';
    form.action = '{% url "web:checkout" %}';
   
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    const csrfInput = document.createElement('input');
    csrfInput.type = 'hidden';
    csrfInput.name = 'csrfmiddlewaretoken';
    csrfInput.value = csrfToken;
    form.appendChild(csrfInput);

    const itemsJsonInput = document.createElement('input');
    itemsJsonInput.type = 'hidden';
    itemsJsonInput.name = 'itemsJson';
    itemsJsonInput.value = JSON.stringify(cart);
    form.appendChild(itemsJsonInput);

    document.body.appendChild(form);
    form.submit();
  }