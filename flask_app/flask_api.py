from flask import Flask, request, jsonify
from http import HTTPStatus
import uuid

app = Flask(__name__)

# Simpan data sementara di list
items = []

@app.route('/items', methods=['GET'])
def get_items():
    """Menampilkan semua item"""
    return jsonify({
        "message": "Daftar semua item berhasil diambil",
        "data": items
    }), HTTPStatus.OK


@app.route('/items', methods=['POST'])
def create_item():
    """Menambahkan item baru"""
    data = request.get_json()

    # Validasi input
    if not data or 'name' not in data or 'price' not in data:
        return jsonify({"error": "Harus ada name dan price"}), HTTPStatus.BAD_REQUEST

    new_item = {
        "id": str(uuid.uuid4()),
        "name": data['name'],
        "price": float(data['price']),
        "category": data.get('category', 'Umum'),
        "description": data.get('description', '')
    }

    items.append(new_item)
    return jsonify({
        "message": "Item baru berhasil ditambahkan",
        "data": new_item
    }), HTTPStatus.CREATED


@app.route('/items/<string:item_id>', methods=['GET'])
def get_item_by_id(item_id):
    """Mendapatkan item berdasarkan ID"""
    for item in items:
        if item['id'] == item_id:
            return jsonify(item), HTTPStatus.OK
    return jsonify({"error": f"Item dengan id {item_id} tidak ditemukan"}), HTTPStatus.NOT_FOUND


@app.route('/items/<string:item_id>', methods=['PUT'])
def update_item(item_id):
    """Memperbarui item"""
    data = request.get_json()
    for item in items:
        if item['id'] == item_id:
            item.update({k: v for k, v in data.items() if v is not None})
            return jsonify({
                "message": "Data item berhasil diperbarui",
                "data": item
            }), HTTPStatus.OK
    return jsonify({"error": "Item tidak ditemukan"}), HTTPStatus.NOT_FOUND


@app.route('/items/<string:item_id>', methods=['DELETE'])
def delete_item(item_id):
    """Menghapus item"""
    for i, item in enumerate(items):
        if item['id'] == item_id:
            del items[i]
            return jsonify({"message": f"Item dengan id {item_id} berhasil dihapus"}), HTTPStatus.OK
    return jsonify({"error": "Item tidak ditemukan"}), HTTPStatus.NOT_FOUND


if __name__ == '__main__':
    app.run(debug=True, port=5001)
