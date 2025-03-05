function clearAfterSubmit(event) {
    if (event.key === 'Enter') { 
      event.preventDefault();   
      const form = document.getElementById('searchForm');
      form.submit();           
      setTimeout(() => {
        document.getElementById('searchInput').value = '';
      }, 100);
    }
  }

  function triggerSearch(event) {
    if (event.key === 'Enter') { 
      event.preventDefault();  
      document.getElementById('searchForm').submit(); 
    }
  }  


  document.getElementById('searchInput').addEventListener('keypress', function(event) {
    if (event.key === 'Enter') {
      event.preventDefault(); 
      document.getElementById('searchForm').submit(); 
    }
  });  