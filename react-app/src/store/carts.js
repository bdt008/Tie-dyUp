
//constants
const GET_CART_DETAILS = "GET_CART_DETAILS";
const CREATE_CART = "CREATE_CART";
const UPDATE_CART = "UPCATE_CART";
const DELETE_CART = "DELETE_CART";
const ADD_PRODUCT_TO_CART = "ADD_PRODUCT_TO_CART";
const DELETE_PRODUCT_FROM_CART = "DELETE_PRODUCT_FROM_CART"

//action creators
  const getCartDetails = (cart) => {
    return {
      type: GET_CART_DETAILS,
      cart,
    };
  };

  const addCart = (cart) => {
    return {
      type: CREATE_CART,
      cart,
    };
  };

  const addProductToCart = (cart) => {
    return {
      type: ADD_PRODUCT_TO_CART,
      cart
    };
  };

  const updateCart = (cart) => {
    return {
      type: UPDATE_CART,
      cart,
    };
  };

  const deleteCart = (cartId) => {
    return {
      type: DELETE_CART,
      cartId,
    };
  };

  const deleteProductFromCart = (cart) => {
    return {
      type: DELETE_PRODUCT_FROM_CART,
      cart,
    };
  };


  //THUNKS

  //get a user's cart
  export const getUserCart = (cartId) => async (dispatch) => {
    const res = await fetch(`/api/carts/${cartId}`);

    if (res.ok) {
        const cart = await res.json();
        dispatch(getCartDetails(cart))
        return res;
    }
    return res;
  }

  //create a cart
  export const createCart = () => async (dispatch) => {
    const res = await fetch('/api/carts', {
      method: 'POST',
      body: JSON.stringify({
        checkout: false
      }),
    });

    if (res.ok) {
      const cart = await res.json();
      dispatch(addCart(cart));
      return res
    }
  };

  //add to cart
  export const addProductCart = (cartId, productId) => async (dispatch) => {
    const res = await fetch(`/api/carts/${cartId}/add_product/${productId}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    });

    if (res.ok) {
      const data = await response.json();
      dispatch(addProductToCart(data));
      return res
    }
  };

  //update cart
  export const editCart = (id) => async (dispatch) => {
    const res = await fetch(`/api/carts/${id}/update`, {
      method: "PUT"
    });

    if (res.ok) {
      const updatedCart = await res.json();
      dispatch(updateCart(updatedCart));
      return res;
    }
  };

  //delete product from cart
  export const removeFromCart = (cart_id, product__id) => async (dispatch) => {
    const res = await fetch(`/api/carts/${cart_id}/deleteProduct/${product_id}`, {
        method: "DELETE"
    })

    const response = await res.json();
    if (res.status === 200) {
        dispatch(deleteProductFromCart(response.cart));
    }
    return response;
  }

  //delete cart
  export const deleteACart = (cartId) => async (dispatch) => {
    const res = await fetch(`/api/carts/${cartId}/delete`, {
      method: "DELETE",
    });
    const response = await res.json();
    if (res.status === 200) {
      dispatch(deleteCart(cartId));
    }
    return response;
  };

  //reducer
  const initialState = {carts: null, currentCart: null};

  export default function cartReducer(state = initialState, action) {
    let newState = {...state };
    switch (action.type) {
      case GET_CART_DETAILS:
        newState.currentCart = {...action.cart} //sets the currentCart property in the state to the cart object passed in the payload
        return newState;
      case CREATE_CART:
        newState.carts[action.cart.id] = {...action.cart}; //adds a new cart object to the carts property using the cart ID as the key and the cart object as the value
        return newState;
      case ADD_ITEM_TO_CART:
        newState.currentCart = {...action.cart}
        return newState;
      case UPDATE_CART:
        newState.currentCart = {...action.cart}
        newState.cart[action.cart.id] = {...action.cart};
        return newState;
      case DELETE_CART:
        delete newState.cart[action.cartId];
        return newState;
      case DELETE_ITEM_FROM_CART:
        newState.currentCart[action.cart.id] = action.cart;
        return newState;
      default:
        return state;
    }
  }
