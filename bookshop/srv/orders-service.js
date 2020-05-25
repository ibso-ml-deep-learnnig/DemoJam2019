const cds = require('@sap/cds')

module.exports = cds.service.impl(function() {

  const { Books, Authors } = cds.entities

  // Reduce stock of ordered books if available stock suffices
  this.before ('CREATE', 'Orders', (req) => {
    //this.emit('submitOrder', req)
    const { Items: OrderItems } = req.data
    const tx = cds.transaction(req)

    return tx.run (()=> OrderItems.map (async order => {
      //check Author of orderd book
      const response = await tx.read(Books).where('ID',order.book_ID);
      if(response[0].author_ID) req.error(409,`Book ${order.book_ID} has no Author`)

      UPDATE (Books) .where ('ID =', order.book_ID)
      .and ('stock >=', order.amount)
      .set ('stock -=', order.amount)
    })) .then (all => all.forEach ((affectedRows,i) => {
      if (affectedRows === 0)  req.error (409,
        `${OrderItems[i].amount} exceeds stock for book #${OrderItems[i].book_ID}`
      )
    }))
  })

  // Reduce stock of ordered books if available stock suffices
  this.on ('submitOrder', async req => {
    const {book,amount} = req.data
    const n = await UPDATE (Books, book)
      .with ({ stock: {'-=': amount }})
      .where ({ stock: {'>=': amount }})
    n > 0 || req.error (409,`${amount} exceeds stock for book #${book}`)
  })  

})
