
//constants
const GET_ALL_PRODUCTS = "GET_ALL_PRODUCTS";
const GET_USER_PRODUCTS = "GET_USER_PRODUCTS";
const GET_PRODUCT_DETAILS = "GET_PRODUCT_DETAILS";
const CREATE_PRODUCT = "CREATE_PRODUCT";
const DELETE_PRODUCT = "DELETE PRODUCT";
const UPDATE_PRODUCT = "UPDATE PRODUCT";

//Action Creators

const getProducts = (products) => {
    return {
        type: GET_ALL_PRODUCTS,
        products,
    };
};

const getUserProducts = (products) => {
    return {
        type: GET_USER_PRODUCTS,
        products,
    };
};

const getProductDetails = (product) => {
    return {
        ype: GET_PRODUCT_DETAILS,
        product
    };
};

const addProduct = (product) => {
    return {
        type: CREATE_PRODUCT.
        product,
    };
};


const deleteProduct = (productId) => {
    return {
        type: DELETE_PRODUCT,
        productId,
    };
};

const updateProduct = (product) => {
    return {
        type: UPDATE_PRODUCT,
        product,
    };
};

//Thunks

//Get all products
export const getAllProducts = () => async (dispatch) => {
    const res = await fetch("/api/products/")

    if (res.ok) {
        const data = await res.json();
        dispatch(getProducts(data.Products));
    }

    return res;

};

//Get user products
export const userProducts = (userId) => async (dispatch) => {
    const res = await fetch(`/api/${userId}/store`); //double check this route

    if (res.ok) {
        const data = await res.json();
        dispatch(getUserProducts(data))
        return res
    } else {
        return res
    };

};

//Get a single product
export const getSingleProduct = (productId) => async (dispatch) => {
    const res = await fetch(`/api/products/${productId}`);

    if (res.ok) {
        const product = await res.json();
        dispatch(getProductDetails(product));
        return res;
    }

    return res;
};

//Create a product
export const createNewProduct = (product) => async (dispatch) => {
    const { name, description, price, image_url, brand, catagory } = product;

    const res = await fetch("/api/products/", {
        method: "POST",
        body: JSON.stringify({
            name,
            description,
            price,
            image_url,
            brand,
            catagory
        }),
    });

    if (res.ok) {
        const newProduct = await res.json();
        dispatch(addProduct(newProduct));
        return res;
    }
};

//Update a product
export const editProduct = (product, id) => async (dispatch) => {
    const res = await fetch(`/api/products/${id}`, {
        method: "PUT",
        body: JSON.stringify(product),
    });

    if (res.ok) {
        const productUpdate = await res.json();
        dispatch(updateProduct(productUpdate));
        return res;
    }
};

//Delete a product
export const deleteAProduct = (productId) = async (dispatch) => {
    const res = await fetch(`/api/products/${productId}`, {
        method: "DELETE",
    });

    if (res.ok) {
        dispatch(deleteProduct(productId))
    }
}

const initialState = {};

//reducer
export default function productReducer (state = initialState, action) {
    let newState = {...state};
    switch (action.type) {
        case GET_ALL_PRODUCTS:
            return {...newState, ...action.payload}
        case GET_USER_PRODUCTS:
            const userProducts = {}; //creating a new object to store user's products
            action.products.forEach((product) => { //looping through each product in 'action.products' to populate object
                userProducts[product.id] = product; //using product's id as the key
            });
            return userProducts //returning the object we created
        case GET_PRODUCT_DETAILS:
            newState[action.product.id] = action.product
            return newState;
        case CREATE_PRODUCT:
            newState[action.product.id] = action.product;
            return newState;
        case UPDATE_PRODUCT:
            newState[action.product.id] = action.product;
            return newState;
        case DELETE_PRODUCT:
            delete newState[action.productId];
            return newState;
        default:
            return state;
    }
}
