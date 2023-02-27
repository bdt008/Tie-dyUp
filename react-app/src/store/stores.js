
//constants
const GET_ALL_STORES = "GET_ALL_STORES";
const GET_USER_STORES = "GET_USER_STORES";
const GET_STORE_DETAILS = "GET_STORE_DETAILS";
const CREATE_STORE = "CREATE_STORE";
const UPDATE_STORE = "UPDATE_STORE";
const DELETE_STORE = "DELETE_STORE";

//Action creators
const getStores = (stores) => {
    return {
        type: GET_ALL_STORES,
        stores,
    };
};

const getUserStores = (stores) => {
    return {
        type: GET_USER_STORES,
        stores,
    };
};

const getStoreDetails = (store) => {
    return {
        type: GET_STORE_DETAILS,
        store,
    };
};

const addStore = (store) => {
    return {
        type: CREATE_STORE,
        store
    }
}

const updateStore = (store) => {
    return {
      type: UPDATE_STORE,
      store,
    };
  };

  const deleteStore = (storeId) => {
    return {
      type: DELETE_STORE,
      storeId,
    };
  };

  //Get all stores
  export const getAllStores = () => async (dispatch) => {
    const res = await fetch("/api/stores/");

    if (res.ok) {
      const data = await res.json();
      dispatch(getStores(data.Stores));
    }
    return res;
  };

  //Get one store
  export const getSingleStore = (storeId) => async (dispatch) => {
    const res = await fetch(`/api/stores/${storeId}`);
    const data = await res.json();
    dispatch(getStoreDetails(store));
    return res;
  };

  //Create a store
  export const createStore = (store) => async (dispatch) => {
    const { name, about, cover_image_url } = store

    const res = await fetch('/api/stores/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(store),
    });
    const data = await res.json();
    dispatch(addStore(data));
    return res;
  };

  //Update a store
  export const editStore = (store, id) => async (dispatch) => {
    const res = await fetch(`/api/stores/${store.id}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(store),
    });
    const data = await res.json();
    dispatch(updateStore(data));
    return res
  };

  //Delete a store
  export const deleteAStore = (storeId) => async (dispatch) => {
    const res = await fetch(`/api/stores/${storeId}`, {
      method: "DELETE",
    });
    const response = await res.json();
    if (res.status === 200) {
      dispatch(deleteStore(storeId));
    }
    return response;
  };

  const initialState = {};

  //reducer
  export default function storeReducer(state = initialState, action) {
    let newState = {...state };
    switch (action.type) {
      case GET_ALL_STORES:
        action.stores.forEach((store) => newState[store.id] = store);
        return newState;
      case GET_USER_STORES:
        let userStores = {};
        action.stores.forEach((store) => userStores[store.id] = store);
        return userStores;
      case GET_STORE_DETAILS:
        newState[action.store.id] = action.store;
        return newState;
      case CREATE_STORE:
        newState[action.store.id] = action.store;
        return newState;
      case UPDATE_STORE:
        newState[action.store.id] = action.store;
        return newState;
      case DELETE_STORE:
        delete newState[action.storeId];
        return newState;
      default:
        return state;
    }
  }
