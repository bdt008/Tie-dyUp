import { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { useParams, useHistory, NavLink } from "react-router-dom";
import { getSingleStore } from "../../store/stores"

import './index.css';

function StorePage() {
    const { storeId } = useParams();  //deconstructing the 'storeId' parameter from the URL
    const store = useSelector((state) => state.storeState[storeId]); //accessing the store object from the Redux Store
    const user = useSelector(state => state.session.user); //accessinf the session Redux store
    const dispatch = useDispatch(); //the dispatch function is used to send an action to the Redux Store
    const history = useHistory(); //the history object is used to manipulate the browser history and navigate through pages.


    useEffect(() => {
        (async() => {
          const res = await dispatch(getSingleStore(storeId));
          if (res.status === 404){
            history.push('/404')
          }
        })();
      }, [dispatch]); //used to fetch a single store when the page refreshes and is directed to a 404 error page if store is not found

      //implement reviews and seeing reviews eventually

      if (!loaded) {
        return null;
      } // will return null while the data is loading so that the componenet can avoid rendering incomplete or broken content on the page


      return (
        <div>
          <h1>Products for Store {storeId}</h1>
          <p>{store.name}</p>
        </div>
      );
    };

export default StorePage;
